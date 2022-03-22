from __future__ import absolute_import, unicode_literals
import requests
from celery.task import task
from django.conf import settings
from django.core.mail import EmailMessage
from .models import Setting
import json

TOKEN = settings.SMART_HOME_ACCESS_TOKEN
url = settings.SMART_HOME_API_URL
headers = {'Authorization': f'Bearer {TOKEN}'}


@task()
def smart_home_manager():
    controller_data = requests.get(url, headers=headers).json().get('data')
    controller_data = {x['name']: x for x in controller_data}
    payload = {
        'controllers': []
    }

    boiler_temperature = controller_data['boiler_temperature']['value']
    hot_water_target_temperature = Setting.objects.get(
        controller_name='hot_water_target_temperature').value

    bedroom_temperature = controller_data['bedroom_temperature']['value']
    bedroom_target_temperature = Setting.objects.get(
        controller_name='bedroom_target_temperature').value

    if controller_data['leak_detector']['value']:
        # если датчик показывает протечку и есть гор. и/или хол. вода,
        # перекрываем гор. и/или хол. воду
        if controller_data['cold_water']['value']:
            payload['controllers'].append({'name': 'cold_water', 'value': False})

        if controller_data['hot_water']['value']:
            payload['controllers'].append({'name': 'hot_water', 'value': False})
        email = EmailMessage(
            'leak detector',
            'text',
            settings.EMAIL_HOST,
            [settings.EMAIL_RECEPIENT],
        )
        email.send(fail_silently=False)

    # если протечка или нет холодной воды
    if controller_data['leak_detector']['value'] or \
            not controller_data['cold_water']['value']:
        if controller_data['boiler']['value']:
            payload['controllers'].append({'name': 'boiler', 'value': False})
        if controller_data['washing_machine']['value'] == 'on':
            payload['controllers'].append({'name': 'washing_machine', 'value': "off"})

    if controller_data['smoke_detector']['value']:
        # если дым, выключаем кондиционер, бойлер и свет, но только если они включены
        if controller_data['air_conditioner']['value']:
            payload['controllers'].append(
                {'name': 'air_conditioner', 'value': False}
            )
        if controller_data['bathroom_light']['value']:
            payload['controllers'].append(
                {'name': 'bathroom_light', 'value': False}
            )
        if controller_data['bedroom_light']['value']:
            payload['controllers'].append(
                {'name': 'bedroom_light', 'value': False}
            )
        if controller_data['boiler']['value']:
            payload['controllers'].append({'name': 'boiler', 'value': False})
        if controller_data['washing_machine']['value'] == 'on':
            payload['controllers'].append(
                {'name': 'washing_machine', 'value': 'off'}
            )

    if not controller_data['leak_detector']['value'] and \
            controller_data['cold_water']['value'] and \
            not controller_data['smoke_detector']['value'] and \
            not controller_data['boiler']['value'] and \
            (boiler_temperature < hot_water_target_temperature * 0.9):
        payload['controllers'].append({'name': 'boiler', 'value': True})

    if controller_data['cold_water']['value'] and \
            boiler_temperature > hot_water_target_temperature * 1.1 and \
            controller_data['boiler']['value']:
        payload['controllers'].append({'name': 'boiler', 'value': False})

    if (bedroom_temperature < bedroom_target_temperature * 0.9) and \
            not controller_data['smoke_detector']['value'] and \
            controller_data['air_conditioner']['value']:
        payload['controllers'].append({'name': 'air_conditioner', 'value': False})

    if not controller_data['smoke_detector']['value'] and \
            not controller_data['air_conditioner']['value'] and \
            bedroom_temperature > bedroom_target_temperature * 1.1:
        payload['controllers'].append({'name': 'air_conditioner', 'value': True})

    outdoor_light = controller_data['outdoor_light']['value']
    bedroom_light = controller_data['bedroom_light']['value']
    if controller_data['curtains']['value'] == 'slightly_open':
        pass
    else:
        if outdoor_light < 50 and not bedroom_light:
            if controller_data['curtains']['value'] == 'close':
                payload['controllers'].append({'name': 'curtains', 'value': 'open'})
        elif outdoor_light > 50 or bedroom_light:
            if controller_data['curtains']['value'] == 'open':
                payload['controllers'].append({'name': 'curtains', 'value': 'close'})

    if payload['controllers']:
        unique = []
        for item in payload['controllers']:
            if item not in unique:
                unique.append(item)
        payload['controllers'] = unique
        requests.post(url, headers=headers, json=payload)

###################################################################################################################
# from __future__ import absolute_import, unicode_literals
# from celery import Celery
# import requests
# from django.core.mail import send_mail
# from django.http import HttpResponse
# from coursera_house import settings
# from .models import Setting
#
# celery = Celery('tasks', broker='amqp://localhost//')
# header = {
#         'Authorization': 'Bearer secret;)'
#     }
#
#
# @celery.task()
# def smart_home_manager():
#
#     try:
#         context = \
#             requests.get(settings.SMART_HOME_API_URL, headers=header)
#         if context.json()['status'] != 'ok':
#             return HttpResponse('Some problems w API', status=502)
#     except:
#         return HttpResponse('Some problems w API', status=502)
#
#     controllers_dict = dict()
#     controllers_dict['controllers'] = []
#     bedroom_light = None
#     curtains = None
#     smoke_detector = None
#     cold_water = None
#     washing_machine = None
#
#     '''controllers_dict['controllers'].append({
#         'name': Setting.objects.get(id=1).controller_name,
#         'value': Setting.objects.get(id=1).value
#     })
#
#     controllers_dict['controllers'].append({
#         'name': Setting.objects.get(id=2).controller_name,
#         'value': Setting.objects.get(id=2).value
#     })'''
#
#     for value in context.json()['data']:
#         if value['name'] == 'washing_machine':
#             washing_machine = value['value']
#
#         if value['name'] == 'bedroom_light':
#             bedroom_light = value['value']
#
#         if value['name'] == 'curtains':
#             curtains = value['value']
#
#         if value['name'] == 'smoke_detector':
#             smoke_detector = value['value']
#
#         if value['name'] == 'leak_detector':
#             leak_detector = value['value']
#             if value['value']:
#                 if {'name': 'cold_water', 'value': False} not in controllers_dict['controllers']:
#                     controllers_dict['controllers'].append({
#                         'name': 'cold_water',
#                         'value': False
#                     })
#                 if {'name': 'hot_water', 'value': False} not in controllers_dict['controllers']:
#                     controllers_dict['controllers'].append({
#                         'name': 'hot_water',
#                         'value': False
#                     })
#
#         if value['name'] == 'cold_water':
#             cold_water = value['value']
#             if not value['value']:
#                 if {'name': 'boiler', 'value': False} not in controllers_dict['controllers']:
#                     controllers_dict['controllers'].append({
#                         'name': 'boiler',
#                         'value': False
#                     })
#                 if {'name': 'washing_machine', 'value': 'off'} not in controllers_dict['controllers'] \
#                         and washing_machine != 'broken':
#                     controllers_dict['controllers'].append({
#                         'name': 'washing_machine',
#                         'value': 'off'
#                     })
#
#         if value['name'] == 'boiler_temperature':
#             if value['value']:
#                 if value['value'] < Setting.objects.get(id=2).value * 0.9 and not smoke_detector and cold_water:
#                     if {'name': 'boiler', 'value': True} not in controllers_dict['controllers']:
#                         controllers_dict['controllers'].append({
#                             'name': 'boiler',
#                             'value': True
#                         })
#
#                 elif value['value'] >= Setting.objects.get(id=2).value * 1.1:
#                     if {'name': 'boiler', 'value': False} not in controllers_dict['controllers']:
#                         controllers_dict['controllers'].append({
#                             'name': 'boiler',
#                             'value': False
#                         })
#
#         if value['name'] == 'outdoor_light':
#             if value['value'] < 50 and not bedroom_light and curtains != 'slightly_open':
#                 if {'name': 'curtains', 'value': 'open'} not in controllers_dict['controllers']:
#                     controllers_dict['controllers'].append({
#                         'name': 'curtains',
#                         'value': 'open'
#                     })
#
#             elif (value['value'] > 50 or bedroom_light) and curtains != 'slightly_open':
#                 if {'name': 'curtains', 'value': 'close'} not in controllers_dict['controllers']:
#                     controllers_dict['controllers'].append({
#                         'name': 'curtains',
#                         'value': 'close'
#                     })
#
#         if smoke_detector:
#             if {'name': 'air_conditioner', 'value': False} not in controllers_dict['controllers']:
#                 controllers_dict['controllers'].append({
#                     'name': 'air_conditioner',
#                     'value': False
#                 })
#             if {'name': 'bedroom_light', 'value': False} not in controllers_dict['controllers']:
#                 controllers_dict['controllers'].append({
#                     'name': 'bedroom_light',
#                     'value': False
#                 })
#             if {'name': 'bathroom_light', 'value': False} not in controllers_dict['controllers']:
#                 controllers_dict['controllers'].append({
#                     'name': 'bathroom_light',
#                     'value': False
#                 })
#             if {'name': 'boiler', 'value': False} not in controllers_dict['controllers']:
#                 controllers_dict['controllers'].append({
#                     'name': 'boiler',
#                     'value': False
#                 })
#             if {'name': 'washing_machine', 'value': 'off'} not in controllers_dict['controllers'] \
#                     and washing_machine != 'broken':
#                 controllers_dict['controllers'].append({
#                     'name': 'washing_machine',
#                     'value': 'off'
#                 })
#
#         if value['name'] == 'bedroom_temperature':
#             if value['value'] > Setting.objects.get(id=1).value * 1.1 and not smoke_detector:
#                 if {'name': 'air_conditioner', 'value': True} not in controllers_dict['controllers']:
#                     controllers_dict['controllers'].append({
#                         'name': 'air_conditioner',
#                         'value': True
#                     })
#
#             elif value['value'] < Setting.objects.get(id=1).value * 0.9:
#                 if {'name': 'air_conditioner', 'value': False} not in controllers_dict['controllers']:
#                     controllers_dict['controllers'].append({
#                         'name': 'air_conditioner',
#                         'value': False
#                     })
#
#     for d in controllers_dict['controllers']:
#         for c in context.json()['data']:
#             if d['name'] == c['name'] and d['value'] == c['value']:
#                 controllers_dict['controllers'].remove(d)
#
#     try:
#         if controllers_dict['controllers']:
#             r = requests.post(settings.SMART_HOME_API_URL, headers=header,
#                               json=controllers_dict)
#             if r.json()['status'] != 'ok':
#                 return HttpResponse('Some problems w API', status=502)
#     except:
#         return HttpResponse('Some problems w API', status=502)
#
#     return controllers_dict['controllers']


