import requests

res = requests.post('http://127.0.0.1:8000/api/v1/goods/',
                   # data={"title": "Gouda cheese 1.", "description": "The number 1 cheese in the world!", "price": 101},
                   json={"title": "sd", "description": "The number 1 cheese in the world!", "price": 5},
                   # auth=('omer', 'b01ad0ce'),
                   headers={'Content-Type': 'application/json'},
                   # params={"title": "Gouda cheese.", "description": "The number 1 cheese in the world!", "price": 101}
                   )
print(res.status_code)
print(res.headers['Content-Type'])
print(res.text)
# json.loads(response.content.decode('utf-8'))

# из консоли -
#
#  $ python -m pytest tests/

# ?title=asdfg&description= asdfg&price=100
# "title": "Gouda cheese.", "description": "The number 1 cheese in the world!", "price": 101
# "text": "Best. Cheese. Ever.", "grade": 9




# from django.http import HttpResponse, JsonResponse
# from django.views import View
# from django import forms
# import json
# from somemart.models import Item, Review
# from django.contrib.auth.mixins import LoginRequiredMixin
#
#
# class ItemForm(forms.Form):
#     title = forms.CharField(min_length=1, max_length=64)
#     description = forms.CharField(min_length=1, max_length=1024)
#     price = forms.IntegerField(min_value=1, max_value=1000000)
#
#
# class ReviewForm(forms.Form):
#     text = forms.CharField(min_length=1, max_length=1024)
#     grade = forms.IntegerField(min_value=1, max_value=10)
#
#
# class AddItemView(LoginRequiredMixin, View):
#     """View для создания товара."""
#
#     def post(self, request):
#         form = ItemForm(request.POST)
#
#         if form.is_valid():
#             context = form.cleaned_data
#             item = Item(title=context['title'], description=context['description'], price=context['price'])
#             item.save()
#             data = {'id': item.pk}
#             return JsonResponse(data, status=201)
#         else:
#             return HttpResponse(status=400)
#
#
# class PostReviewView(View):
#     """View для создания отзыва о товаре."""
#
#     def post(self, request, item_id):
#         form = ReviewForm(request.POST)
#         data = {'id': item_id}
#
#         if form.is_valid():
#             context = form.cleaned_data
#             try:
#                 item = Item.objects.get(pk=item_id)
#                 review = Review(text=context['text'], grade=context['grade'], item=item)
#                 review.save()
#                 return JsonResponse(data, status=201)
#             except Item.DoesNotExist:
#                 return HttpResponse(status=404)
#         else:
#             return HttpResponse(status=400)
#
#
# class GetItemView(View):
#     """View для получения информации о товаре.
#
#     Помимо основной информации выдает последние отзывы о товаре, не более 5
#     штук.
#     """
#
#     def get(self, request, item_id):
#         try:
#             item = Item.objects.get(pk=item_id)
#             reviews = [
#                 {
#                     'id': review.pk,
#                     'text': review.text,
#                     'grade': review.grade
#                 }
#                 for review in Review.objects.filter(item=item).order_by('-pk')
#             ]
#
#             data = {
#                 'id': item.pk,
#                 'title': item.title,
#                 'description': item.description,
#                 'price': item.price,
#                 'reviews': reviews[-5:]
#             }
#             return JsonResponse(data, status=200)
#         except (Item.DoesNotExist, json.JSONDecodeError):
#             return HttpResponse(status=404)
#


# import json
# from marshmallow import Schema, fields, ValidationError
# from marshmallow.validate import Length, Range
# from django.http import HttpResponse, JsonResponse
# from django.views import View
# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator
# from django.forms.models import model_to_dict
# from .models import Item, Review
#
#
# @method_decorator(csrf_exempt, name='dispatch')
# class AddItemView(View):
#     """View для создания товара."""
#
#     def post(self, request):
#         try:
#             document = json.loads(request.body)
#             schema = AddItemReview(strict=True)
#             valid_data = schema.load(document)
#             item = Item(title=valid_data.data['title'],
#                         description=valid_data.data['description'],
#                         price=valid_data.data['price'])
#             item.save()
#             data = {'id': item.pk}
#             return JsonResponse(data, status=201)
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON'}, status=400)
#         except ValidationError as e:
#             return JsonResponse({'error': e.messages}, status=400)
#
#
#
# @method_decorator(csrf_exempt, name='dispatch')
# class PostReviewView(View):
#     """View для создания отзыва о товаре."""
#
#     def post(self, request, item_id):
#         try:
#             document = json.loads(request.body)
#             schema = PostItemReview(strict=True)
#             valid_data = schema.load(document)
#             review = Review(text=valid_data.data['text'],
#                             grade=valid_data.data['grade'],
#                             item=Item.objects.get(pk=item_id))
#             review.save()
#             data = {'id': item_id}
#             return JsonResponse(data, status=201)
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Invalid JSON'}, status=400)
#         except ValidationError as e:
#             return JsonResponse({'error': e.messages}, status=400)
#         except Exception as e:
#             return JsonResponse({'error': 'no such id'}, status=404)
#
#
#
# class GetItemView(View):
#     """View для получения информации о товаре.
#
#     Помимо основной информации выдает последние отзывы о товаре, не более 5
#     штук.
#     """
#
#     def get(self, request, item_id):
#         try:
#             entries = Review.objects.all().order_by('-id')
#             item = Item.objects.get(pk=item_id)
#             data = model_to_dict(item)
#             data["reviews"] = []
#             if len(entries) > 5:
#                 entries = entries[:5]
#                 for entry in entries:
#                     data["reviews"].append(model_to_dict(entry))
#             else:
#                 for entry in entries:
#                     data["reviews"].append(model_to_dict(entry))
#             return JsonResponse(data, status=200)
#         except Exception as e:
#             return JsonResponse({'error': 'no such id'}, status=404)
#
#
# class AddItemReview(Schema):
#     title = fields.Str(validate=Length(1, 64), required=True)
#     description = fields.Str(validate=Length(1, 1024), required=True)
#     price = fields.Int(validate=Range(1, 1000000), required=True)
#
#
# class PostItemReview(Schema):
#     text = fields.Str(validate=Length(1, 1024), required=True)
#     grade = fields.Int(validate=Range(1, 10), required=True)
#
#
#
# import json
# from django import forms
#
# class SomeForm(forms.Form):
#     name = forms.CharField(label=u'Name', max_length=25)
#
# def some_view(request):
#     json_string = request.POST.get('json_data')
#     form_data = json.loads(json_string)[0]  # data = json.loads(request.body.decode())
#     f = SomeForm(form_data)
#     if f.is_valid():
#         name = f.cleaned_data['name']
#         # ... Работа с данными ...
#     else:
#         # ... Обработка ошибки ...