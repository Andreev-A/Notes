from django.http import JsonResponse
from django.shortcuts import render

from django.views import View
from .forms import DummyForm

import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError
from .schemas import REVIEW_SCHEMA, ReviewSchema

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from marshmallow import ValidationError as MarshmallowError

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import Feedback


class FeedbackCreateView(LoginRequiredMixin, CreateView):
    model = Feedback
    fields = ['text', 'grade', 'subject']
    success_url = '/feedback/add'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



@method_decorator(csrf_exempt, name='dispatch')
class SchemaView(View):

    def post(self, request):
        try:
            document = json.loads(request.body)
            validate(document, REVIEW_SCHEMA)
            return JsonResponse(document, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'errors': 'Invalid JSON'}, status=400)
        except ValidationError as exc:
            return JsonResponse({'errors': exc.message}, status=400)

# curl -v -H "Content-Type: application/json" -X POST -d '{"grade":42,"feedback":hello"}' http://127.0.0.1:8000/form/
# http://127.0.0.1:8000/form/
# curl -v -H "Content-Type: application/json;charset=UTF-8" -X POST -d '{"title": "Gouda cheese",
# "description": "The number one cheese in the world", "price": 100}' http://127.0.0.1:8000/api/v1/goods/

@method_decorator(csrf_exempt, name='dispatch')
class MarshView(View):

    def post(self, request):
        try:
            document = json.loads(request.body)
            schema = ReviewSchema(strict=True)
            data = schema.load(document)
            return JsonResponse(data.data, status=201)
        except json.JSONDecodeError:
            return JsonResponse({'errors': 'Invalid JSON'}, status=400)
        except MarshmallowError as exc:
            return JsonResponse({'errors': exc.message}, status=400)
