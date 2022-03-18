import requests
import json
from pprint import pprint

# res = requests.post('http://127.0.0.1:8000/api/v1/goods/',
#                    # data={"title": "Gouda cheese 1.", "description": "The number 1 cheese in the world!", "price": 101},
#                    json={"title": "sd", "description": "The number 1 cheese in the world!", "price": 5},
#                    # auth=('omer', 'b01ad0ce'),
#                    headers={'Content-Type': 'application/json'},
#                    # params={"title": "Gouda cheese.", "description": "The number 1 cheese in the world!", "price": 101}
#                    )
# data=json.dumps(payload)  payload = {'some':'data'} передать в json

# print(res.status_code)
# print(res.headers['Content-Type'])
# pprint(res.text)
# print(json.loads(res.text))  # раскодирование кириллицы

######################################################################################################################
url = 'http://smarthome.webpython.graders.eldf.ru/api/user.controller'
payload = json.dumps({
    "controllers": [
        {
            "name": "air_conditioner",
            "value": True
        },
        {
            "name": "bedroom_light",
            "value": True
        }
    ]
})
headers={
    'Authorization': 'Bearer 787358f3c98a66cec191aaa7c3e3995b22c168276869c7d7a37edc9b6ee4814a',
    'Content-Type': 'application/json'
}
response = requests.request('POST', url, headers=headers, data=payload)
pprint(response.json())

# x = {"controllers": [{"value": False, "name": "air_conditioner"}, {"value": False, "name": "bedroom_light"},
#                      {"value": False, "name": "smoke_detector"}, {"value": False, "name": "bedroom_presence"},
#                      {"value": False, "name": "bedroom_motion"}, {"value": False, "name": "boiler"},
#                      {"value": False, "name": "cold_water"}, {"value": False, "name": "hot_water"},
#                      {"value": False, "name": "bathroom_light"}, {"value": False, "name": "bathroom_motion"},
#                      {"value": False, "name": "bathroom_presence"}, {"value": "close", "name": "curtains"},
#                      {"value": "off", "name": "washing_machine"}, {"value": 76, "name": "bedroom_temperature"},
#                      {"value": 80, "name": "boiler_temperature"}, {"value": False, "name": "leak_detector"},
#                      {"value": 68, "name": "outdoor_light"}]}
#
# answer = requests.post('https://smarthome.webpython.graders.eldf.ru/api/user.controller', headers=headers, data=x)

# res = requests.get('http://smarthome.webpython.graders.eldf.ru/api/auth.current',
#                    headers={'Authorization': 'Bearer 787358f3c98a66cec191aaa7c3e3995b22c168276869c7d7a37edc9b6ee4814a'})

# res = requests.get('http://smarthome.webpython.graders.eldf.ru/api/user.controller',
#                    headers={'Authorization': 'Bearer 787358f3c98a66cec191aaa7c3e3995b22c168276869c7d7a37edc9b6ee4814a'})

# res = requests.post('http://smarthome.webpython.graders.eldf.ru/api/user.controller',
#                     headers={
#                         'Authorization': 'Bearer 787358f3c98a66cec191aaa7c3e3995b22c168276869c7d7a37edc9b6ee4814a',
#                         'Content-Type': 'application/json'
#                         },
#                     data=json.dumps({
#                         "controllers": [
#                             {
#                                 "name": "air_conditioner",
#                                 "value": False
#                             },
#                             {
#                                 "name": "bedroom_light",
#                                 "value": False
#                             }
#                         ]
#                     })
#                     )
# print(res.status_code)
# print(res.headers['Content-Type'])
# pprint(res.text)
# print(json.loads(res.text))  # раскодирование кириллицы


####################################################################################################################

# TypeError: argument of type 'WindowsPath' is not iterable - in django python [duplicate]
# I got this cleared by changing DATABASES in settings.py file:
#
# change
#
# 'NAME': BASE_DIR / 'db.sqlite3',
# to
#
# 'NAME': str(os.path.join(BASE_DIR, "db.sqlite3"))
# this works
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': str(os.path.join(BASE_DIR, "db.sqlite3"))
#     }
# }

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
