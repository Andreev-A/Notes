# API (англ. Application Programming Interface) - это набор определений, протоколов и инструментов для разработки ПО и
# приложений. API-интерфейс разрабатывается для упрощения создания программ, путем предоставления всех необходимых
# функциональных блоков.
# API какого-нибудь модуля или сервиса - это набор функций, констант и методов, которые мы можем использовать. И при
# этом про каждую из них известно, что она принимает, что она возвращает и что она должна делать. Но при этом может
# быть не известно как она это делает.
# Далее рассматрим работу с Web API на примере сервиса, предоставляющего прогноз погоды https://openweathermap.org/api
# Почти все сервисы, предоставляющие API, требуют получить API ключ для того, чтобы можно было пользоваться их API. Это
# связано с тем, что мы должны представиться сервису. Он должен знать, кто делает данный запрос. И при этом они могут
# собирать статистику: кто делает запросы, в какой время, из каких регионов.
# К API-ключу нужно относиться как к конфиденциальным данным. В контексте курса это, конечно, не критично, но если
# кто-то другой будет отправлять запросы от вашего имени, используя ваш ключ, то ваш аккаунт в сервисе
# заблокировать. В API социальных сетей, как правило, есть функции создания и удаления постов.
# Решение: запишите ваш API-ключ в переменную среды (environment variable) операционной системы. Чтобы прочитать
# переменную среды из Python, используйте функцию os.getenv(name)

# import requests
#
# api_url = "http://api.openweathermap.org/data/2.5/weather"
#
# city = input("City? ")
#
# metric = {  # если поставить параметр lang=ru то можно уже получить ответ на русском
#     'q': city,                                    # 9b31719b07e6f8975bc6c4a9e3c54ce0
#     'appid': '11c0d3dc6093f7442898ee49d2430d20',  # 'appid': 'fe6c9ac08e96ecdd33f559f07bc59da7'
#     'units': 'metric'                             # "aa2e2c84ed4a53a0941701439de11f0b"
# }
#
# res = requests.get(api_url, metric=metric)
# # print(res.status_code)
# # print(res.headers["Content-Type"])
# # print(res.json())  # returns json.loads(res.text) :)
#
# data = res.json()
# template = 'Current temperature in {} is {}'
# print(template.format(city, data["main"]["temp"]))



# PyOWM - это клиентская библиотека-оболочка Python для веб-API OpenWeatherMap (OWM). Он позволяет быстро и легко
# использовать данные OWM из приложений Python с помощью простой объектной модели и в удобной для человека форме.
# PyOWM работает на Python 3.7+
# Какие данные я могу получить с помощью PyOWM?
# С PyOWM вы можете интегрировать в свой код любой из следующих веб-API OpenWeatherMap:
# Weather API v2.5 + OneCall API , предоставляющий текущие данные о погоде, прогнозы погоды, историю погоды
# Agro API v1.0 , обеспечивающий поиск и загрузку данных о почве и спутниковых снимков
# Air Pollution API v3.0 , предоставляющий данные о CO, O3, NO2 и SO2
# UV Index API v3.0 , предоставляющий данные об ультрафиолетовой экспозиции
# Stations API v3.0 , позволяющий создавать и управлять метеостанциями, а также публиковать локальные измерения погоды.
# Weather Alerts API v3.0 , позволяющий устанавливать триггеры для погодных условий и областей и опрашивать созданные
# предупреждения
# Плитки изображений для нескольких слоев карты, предоставленные OWM
# Geocoding API v1.0, позволяющий выполнять прямое / обратное геокодирование
#
# from  pyowm  import  OWM
# from  pyowm.utils  import  config
# from  pyowm.utils  import  timestamps
#
# # ---------- Примеры БЕСПЛАТНЫХ КЛЮЧЕЙ API ---------------------
#
# owm  =  OWM ( 'ваш бесплатный ключ API OWM' )
# mgr  =  owm . weather_manager ()
#
#
# # Найдите текущую погоду в Лондоне (Великобритания) и получите подробное
# наблюдение  =  mgr . weather_at_place ( 'Лондон, Великобритания' )
# w  =  наблюдение . Погода
#
# ш . detail_status          # 'облака'
# w . wind ()                   # {'speed': 4.6, 'deg': 330}
# w . влажность                 # 87
# вт . temperature ( 'celsius' )   # {'temp_max': 10,5, 'temp': 9,7, 'temp_min': 9,0}
# w . дождь                     # {}
# ш . heat_index               # Нет
# w . облака                   # 75
#
# # Будет ли ясно завтра в это время в Милане (Италия)?
# прогноз  =  мгр . прогноз_at_place ( 'Милан, ИТ' ,  'ежедневно' )
# answer  =  прогноз . will_be_clear_at ( отметки времени . завтра ())
#
# # ---------- Пример ПЛАТНОГО КЛЮЧА API ---------------------
#
# config_dict  =  config . get_default_config_for_subscription_type ( 'professional' )
# owm  =  OWM ( 'ваш платный ключ API OWM' ,  config_dict )
#
# # Какая сейчас влажность в Берлине (Германия)?
# one_call_object  =  мгр . one_call ( лат = 52,5244 ,  долгота = 13,4105 )
# one_call_object . текущий . влажность

# import pyowm
# owm = pyowm.OWM('11c0d3dc6093f7442898ee49d2430d20')
# mgr = owm.weather_manager()
# city = input('Город: ')  # Saint Petersburg, Ru
# observation = mgr.weather_at_place(city)
# w = observation.weather
# wind = w.wind()
# clouds = w.detailed_status
# temperature = round(w.temperature('celsius')['temp'], 1)
# print(input_file'In {city} now {temperature}°C, {clouds}.')

# Если у кого-то будет ошибка KeyError или list indices must be integers or slices, not str, то кажется дело в новом
# формате json.
# У меня заработало вот это:
# print(template.format(city, data['list'][2]['main']['temp']))
# вместо
# print(template.format (city, data['main']['temp']))

# Как вставить символ градуса?
# print(u"\u00b0")
# "\u2103" для значка "градус Цельсия", то есть с буквой С

# Удобный (и быстрый) способ получения ссылки для запроса:
# input_file'http://numbersapi.com/{i}/math?json'

# Может пригодится кому: проверка статус кода не всегда дает 200. Можно поставить таймаут:
# res = requests.get(url, metric, timeout = 5)

# Если вдруг кто не в курсе, то есть очень приятный вывод json'a с помощью модуля pprint.
# from pprint import pprint
# pprint(json-file)

# В этой задаче вам необходимо воспользоваться API сайта numbersapi.com
# Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.
# Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
# Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.
# Пример запроса к интересному числу:
# http://numbersapi.com/31/math?json=true
# Пример запроса к скучному числу:
# http://numbersapi.com/999/math?json=true
#
# import requests
# with open('D:\\dataset_24476_3.txt', 'r') as input_file:
#     for number in input_file:
#         api_url = "http://numbersapi.com/" + number.strip() + "/math?json=true"
#         res = requests.get(api_url)  # requests.get(input_file'http://******.com/{i}/****')
#         print('Interesting' if res.json()['found'] else 'Boring')
#
# import requests as re
# with open('dataset_24476_3.txt') as file:
#     for num in file:
#         response = re.get('http://numbersapi.com/{number}/math?json=true'.format( number=num.rstrip() )).json()
#         print('Interesting') if response['found'] else print('Boring')
#
# import requests
# import json
# def is_interesting(x):  # пример правильного решения
#     url = "http://numbersapi.com/" + str(x) + "/math?json=true"
#     resp = requests.get(url).text
#     js = json.loads(resp)
#     return js["found"]
# with open("input.txt") as fi:
#     for line in fi:
#         print("Interesting" if is_interesting(line.rstrip()) else "Boring")

# В этой задаче вам необходимо воспользоваться API сайта artsy.net
# API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.
# В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).
# Вам даны идентификаторы художников в базе Artsy.
# Для каждого идентификатора получите информацию о имени художника и годе рождения.
# Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения,
# выведите их имена в лексикографическом порядке.
# Чтобы начать работу с API проекта Artsy, вам необходимо пройти на стартовую страницу документации к API
# https://developers.artsy.net/v2/start и выполнить необходимые шаги, а именно зарегистрироваться, создать приложение, и
# получить пару идентификаторов Client Id и Client Secret. Не публикуйте эти идентификаторы.
# Примечание:
# В качестве имени художника используется параметр sortable_name в кодировке UTF-8.
# Пример входных данных:
# 4d8b92b34eb68a1b2c0003f4
# 537def3c139b21353f0006a6
# 4e2ed576477cc70001006f99
# Пример выходных данных:
# Abbott Mary
# Warhol Andy
# Abbas Hamra
# Примечание для пользователей Windows
# При открытии файла для записи на Windows по умолчанию используется кодировка CP1251, в то время как для записи имен на
# сайте используется кодировка UTF-8, что может привести к ошибке при попытке записать в файл имя с необычными символами
# . Вы можете использовать print, или аргумент encoding функции open.
import requests
import json
out = []
with open('D:\\dataset_24476_4.txt', 'r') as f:
    for code in f:
        client_id = '3c53a2e4f8890e31afec'  # пароль сайта Aaa131102
        client_secret = 'cd6094668288daabad71cf419a49b2bb'
        # инициируем запрос на получение токена
        r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                          data={
                              "client_id": client_id,
                              "client_secret": client_secret
                          })
        # r.encoding = 'utf-8'
        # разбираем ответ сервера
        j = json.loads(r.text)
        # достаем токен
        token = j["token"]
        # создаем заголовок, содержащий наш токен
        headers = {"X-Xapp-Token" : token}
        # инициируем запрос с заголовком
        r = requests.get("https://api.artsy.net/api/artists/" + code.strip(), headers=headers)
        # разбираем ответ сервера
        j = json.loads(r.text)
        out.append(j['birthday'] + j['sortable_name'])
for c in sorted(out):
    print("{}".format(c[4:]))

# import requests
# import json
# # put your id and secret here
# client_id = '...'  # пример правильного решения
# client_secret = '...'
# resp = requests.post("https://api.artsy.net/api/tokens/xapp_token", data={"client_id" : client_id, "client_secret" : client_secret}).text
# token = json.loads(resp)["token"]
#
# def get_json(url):
#     headers = {"X-Xapp-Token" : token}
#     resp = requests.get(url, headers=headers).text
#     return json.loads(resp)
# ans = []
# with open("input.txt") as inp:
#     for id in inp:
#         id = id.rstrip()
#         js = get_json("https://api.artsy.net/api/artists/" + id)
#         ans.append((js["birthday"], js["sortable_name"]))
#
# ans.sort(name=lambda x: (int(x[0]), x[1]))
# print("\n_test".join(map(lambda x: x[1], ans)))

# res = []
# with open('dataset_24476_4.txt', 'r') as input_file, open('result_dict.txt', 'w', encoding='utf-8') as w:
#     for i in input_file:
#         req_str = 'https://api.artsy.net/api/artists/' + i.rstrip()
#         j = requests.get(req_str, headers=headers).json()
#         res.append(j['birthday']+j['sortable_name'])
#     for i in sorted(res):
#         w.write(i[4:]+'\n_test')

