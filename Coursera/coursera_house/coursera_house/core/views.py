from django.urls import reverse_lazy
from django.views.generic import FormView
from .tasks import smart_home_manager
from .models import Setting
from coursera_house import settings
import requests
from django.http import HttpResponse
from .form import ControllerForm

TOKEN = settings.SMART_HOME_ACCESS_TOKEN
url = settings.SMART_HOME_API_URL
headers = {'Authorization': f'Bearer {TOKEN}'}


class ControllerView(FormView):
    form_class = ControllerForm
    template_name = 'core/control.html'
    success_url = reverse_lazy('form')
    header = {
        'Authorization': 'Bearer secret'
    }
    initial = {}
    good_dict = None

    def get(self, request, *args, **kwargs):
        try:
            r = requests.get(
                settings.SMART_HOME_API_URL,
                headers=ControllerView.header)
            if r.json()['status'] != 'ok':
                return HttpResponse('Some problems w API', status=502)
        except:
            return HttpResponse('Some problems w API', status=502)

        api_data = r.json()
        good_dict = dict()

        for d in api_data['data']:
            good_dict[d['name']] = d['value']

        self.good_dict = good_dict

        self.initial = {
            'bedroom_target_temperature': Setting.objects.get(id=1).value if Setting.objects.get(id=1).value
            else 21,

            'hot_water_target_temperature': Setting.objects.get(id=2).value if Setting.objects.get(id=2).value
            else 80,

            'bathroom_light': [x['value'] for x in r.json()['data'] if x['name'] == 'bathroom_light'][0],

            'bedroom_light': [x['value'] for x in r.json()['data'] if x['name'] == 'bedroom_light'][0]
                }

        return super(ControllerView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ControllerView, self).get_context_data(**kwargs)
        context['data'] = self.good_dict

        return context

    def get_initial(self):
        return self.initial

    def form_valid(self, form):

        try:
            r = requests.get(
                settings.SMART_HOME_API_URL,
                headers=ControllerView.header)
            if r.json()['status'] != 'ok':
                return HttpResponse('Some problems w API', status=502)
        except:
            return HttpResponse('Some problems w API', status=502)

        api_data = r.json()
        good_dict = dict()

        for d in api_data['data']:
            good_dict[d['name']] = d['value']

        to_controllers = []
        if good_dict['bedroom_light'] != form.cleaned_data['bedroom_light']:
            to_controllers.append(
                {'name': 'bedroom_light', 'value': form.cleaned_data['bedroom_light']})
        if good_dict['bathroom_light'] != form.cleaned_data['bathroom_light']:
            to_controllers.append(
                {'name': 'bathroom_light', 'value': form.cleaned_data['bathroom_light']})
        if len(to_controllers) != 0:
            to_controllers = {'controllers': to_controllers}
            try:
                r = requests.post(
                    settings.SMART_HOME_API_URL,
                    headers=ControllerView.header,
                    json=to_controllers)
                if r.json()['status'] != 'ok':
                    return HttpResponse('Some problems w API', status=502)
            except:
                return HttpResponse('Some problems w API', status=502)

        object_1 = Setting.objects.get(id=1)
        object_1.value = form.cleaned_data['bedroom_target_temperature']
        object_1.save()
        object_2 = Setting.objects.get(id=2)
        object_2.value = form.cleaned_data['hot_water_target_temperature']
        object_2.save()

        return super(ControllerView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        return super(ControllerView, self).post(request, *args, **kwargs)

####################################################################################################################
# import requests
# from django.conf import settings
# from django.urls import reverse_lazy
# from django.views.generic import FormView
#
# from .models import Setting
# from .form import ControllerForm
#
# TOKEN = settings.SMART_HOME_ACCESS_TOKEN
# url = settings.SMART_HOME_API_URL
# headers = {'Authorization': f'Bearer {TOKEN}'}
#
#
# def get_or_update(controller_name, label, value):
#     try:
#         entry = Setting.objects.get(controller_name=controller_name)
#     except Setting.DoesNotExist:
#         Setting.objects.create(
#             controller_name=controller_name,
#             label=label,
#             value=value
#         )
#     else:
#         entry.value = value
#         entry.save()
#
#
# class ControllerView(FormView):
#     form_class = ControllerForm
#     template_name = 'core/control.html'
#     success_url = reverse_lazy('form')
#
#     def get(self, request, *args, **kwargs):
#         context = self.get_context_data()
#         if not context.get('data'):
#             return self.render_to_response(context, status=502)
#         return self.render_to_response(context)
#
#
#     def get_context_data(self, **kwargs):
#         context = super(ControllerView, self).get_context_data()
#         headers = {'Authorization': f'Bearer {settings.SMART_HOME_ACCESS_TOKEN}'}
#         try:
#             current_controller_data = requests.get(
#                 settings.SMART_HOME_API_URL, headers=headers
#             ).json()
#             context['data'] = current_controller_data
#         except:
#             context['data'] = {}
#         return context
#
#     def get_initial(self):
#         initial = super(ControllerView, self).get_initial()
#         initial['bedroom_target_temperature'] = 21
#         initial['hot_water_target_temperature'] = 80
#         return initial
#
#     def form_valid(self, form):
#         get_or_update(
#             'bedroom_target_temperature',
#             'Bedroom target temperature',
#             form.cleaned_data['bedroom_target_temperature']
#         )
#         get_or_update(
#             'hot_water_target_temperature',
#             'Hot water target temperature value',
#             form.cleaned_data['hot_water_target_temperature']
#         )
#         controller_data = requests.get(url, headers=headers).json().get('data')
#         if controller_data:
#             controller_bedroom_light = list(
#                 filter(lambda x: 'bedroom_light' in x.values(), controller_data)
#             )[0]['value']
#             controller_bathroom_light = list(
#                 filter(lambda x: 'bathroom_light' in x.values(), controller_data)
#             )[0]['value']
#             smoke_detector = list(
#                 filter(lambda x: 'smoke_detector' in x.values(),
#                        controller_data)
#             )[0]['value']
#             payload = {'controllers': []}
#             if not smoke_detector:
#                 if form.cleaned_data['bedroom_light'] != controller_bedroom_light:
#                     payload['controllers'].append(
#                         {'name': 'bedroom_light', 'value': form.cleaned_data['bedroom_light']})
#                 if form.cleaned_data['bathroom_light'] != controller_bathroom_light:
#                     payload['controllers'].append(
#                         {'name': 'bathroom_light', 'value': form.cleaned_data['bathroom_light']})
#                 requests.post(url, headers=headers, json=payload)
#
#         return super(ControllerView, self).get(form)


