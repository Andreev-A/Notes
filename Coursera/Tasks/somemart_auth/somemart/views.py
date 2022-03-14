import json
from django import forms
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from django.utils.decorators import method_decorator

from .models import Item, Review

import base64
from functools import wraps
from django.contrib.auth import authenticate

class GoodForm(forms.Form):
    title = forms.RegexField(min_length=1, max_length=64, regex='\D')
    description = forms.RegexField(min_length=1, max_length=1024, regex='\D')
    price = forms.IntegerField(min_value=1, max_value=1000000)


class ReviewForm(forms.Form):
    text = forms.RegexField(min_length=1, max_length=1024, regex='\D')
    grade = forms.IntegerField(min_value=1, max_value=10)

def basicauth(view_func):
    """Декоратор реализующий HTTP Basic AUTH."""
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if 'HTTP_AUTHORIZATION' in request.META:
            auth = request.META['HTTP_AUTHORIZATION'].split()
            if len(auth) == 2:
                if auth[0].lower() == 'basic':
                    token = base64.b64decode(auth[1].encode('ascii'))
                    username, password = token.decode('utf-8').split(':')
                    user = authenticate(username=username, password=password)
                    if user is not None and user.is_active:
                        request.user = user
                        return view_func(request, *args, **kwargs)

        response = HttpResponse(status=401)
        response['WWW-Authenticate'] = 'Basic realm="Somemart staff API"'
        return response
    return _wrapped_view


def staff_required(view_func):
    """Декоратор проверяющший наличие флага is_staff у пользователя."""
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_staff:
            return view_func(request, *args, **kwargs)
        response = HttpResponse(status=403)
        return response
    return _wrapped_view


@method_decorator(basicauth, name='dispatch')
@method_decorator(staff_required, name='dispatch')
@method_decorator(csrf_exempt, name='dispatch')
class AddItemView(View):
    """View для создания товара."""

    def post(self, request):
        try:
            form_data = json.loads(request.body)
            form = GoodForm(form_data)
            if form.is_valid():
                context = form.cleaned_data
                item = Item(title=context['title'],
                            description=context['description'],
                            price=context['price'])
                item.save()
                data = {'id': item.pk}
                return JsonResponse(data, status=201)
            else:
                return HttpResponse(status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)


@method_decorator(csrf_exempt, name='dispatch')
class PostReviewView(View):
    """View для создания отзыва о товаре."""

    def post(self, request, item_id):
        try:
            form_data = json.loads(request.body)
            form = ReviewForm(form_data)

            if form.is_valid():
                context = form.cleaned_data
                try:
                    item = Item.objects.get(pk=item_id)
                    review = Review(text=context['text'],
                                    grade=context['grade'],
                                    item=item)
                    review.save()
                    return JsonResponse({'id': review.id}, status=201)
                except Item.DoesNotExist:
                    return HttpResponse(status=404)
            else:
                return HttpResponse(status=400)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)


class GetItemView(View):
    """View для получения информации о товаре.
    """

    def get(self, request, item_id):
        try:
            item = Item.objects.prefetch_related('review_set').get(id=item_id)
        except Item.DoesNotExist:
            return JsonResponse(status=404, data={})
        item_dict = model_to_dict(item)
        item_reviews = [model_to_dict(x) for x in item.review_set.all()]
        item_reviews = sorted(
            item_reviews, key=lambda review: review['id'], reverse=True)[:5]
        for review in item_reviews:
            review.pop('item', None)
        item_dict['reviews'] = item_reviews
        return JsonResponse(item_dict, status=200)
