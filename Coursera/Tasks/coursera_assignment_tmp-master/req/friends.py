# Практика по requests
# В этом задании вы научитесь работать с библиотекой requests (https://requests.kennethreitz.org/en/master/), а также
# научитесь работать с API сервиса VK и его документаций, что является достаточно частой задачей разработчика.
# Необходимо написать клиент к API VK , который будет считать распределение возрастов друзей для указанного пользователя.
# То есть на вход подается username или user_id пользователя, на выходе получаем список пар (<возраст>, <количество
# друзей с таким возрастом>), отсортированный по убыванию по второму ключу (количество друзей) и по возрастанию по
# первому ключу (возраст). Например: [(26, 8), (21, 6), (22, 6), (40, 2), (19, 1), (20, 1)]
# Для выполнения задания необходимо использовать шаблон проекта: https://github.com/alexopryshko/coursera_assignment_tmp
# Решение должно быть файлом req/friends.py. В этом файле представлен шаблон функции calc_age, реализацию которой нужно
# написать.
# Для этого вам понадобятся два метода API VK:
# 1. Метод для получения id пользователя (https://vk.com/dev/users.get). Он необходим, так как на вход может подаваться
# username пользователя. URL запроса к API VK: https://api.vk.com/method/users.get
# 2. Метод для получения списка друзей пользователя (https://vk.com/dev/friends.get). URL запроса к API VK:
# https://api.vk.com/method/friends.get
# Для доступа к этим методам вам понадобится  “Сервисный ключ доступа”:
# https://vk.com/dev/access_token?f=3.%20%D0%A1%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D0%BD%D1%8B%D0%B9%20%D0%BA%D0%BB%D1%8E%D1
# %87%20%D0%B4%D0%BE%D1%81%D1%82%D1%83%D0%BF%D0%B0
# Получение сервисного ключа:
# 1. Создать новое приложение, перейдя по ссылке  https://vk.com/apps?act=manage
# 2. После создания приложения, перейти в раздел “настройки” и скопировать “Сервисный ключ доступа”.
# Если нет возможности получить сервисный ключ, то можно использовать уже созданный:
# ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'
# В итоге запросы будут иметь вид:
# – Для получения id пользователя по username или user_id:
# https://api.vk.com/method/users.get?v=5.71&access_token=[token]&user_ids=[user_id]
# – Для получения списка друзей:
# https://api.vk.com/method/friends.get?v=5.71&access_token=[token]&user_id=[user_id]&fields=bdate
# При решении задания обратите внимание на несколько моментов.
# В запросе мы  используем версию  API VK - «5.81».
# В запросе получения списка друзей добавлен ключ fields=bdate.  Он необходим для того, чтобы API сразу вернуло
# пользователей с датами рождения.
# При анализе ответа, полученного методом friends.get, можно заметить,  что bdate есть не у всех пользователей и у
# некоторых в bdate отсутствует год рождения. Поэтому необходимо пропускать этот случай. Примеры возможных значений:
# "bdate":"6.6", "bdate":"25.8.1993".Для вычисления возраста, необходимо взять текущий год , и вычесть из него год
# рождения пользователя, полученный из API (без учета месяца и числа).
# В своем решении вы можете (если необходимо) определять дополнительные функции и импортировать модули.

import requests
from json.decoder import JSONDecodeError
import datetime

ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da' \
               '72454d235c274f1a2be5f45ee711'
API_URL = 'https://api.vk.com/method'
V = '5.81'


def calc_age(uid):
    try:
        payload = {'access_token': ACCESS_TOKEN, 'user_ids': uid, 'v': V}
        r = requests.get(f'{API_URL}/users.get', params=payload)
        ids = r.json()['response'][0]['id']
    except (JSONDecodeError, IndexError, KeyError):
        ids = None

    try:
        payload = {'access_token': ACCESS_TOKEN, 'user_id': ids, 'v': V,
                   'fields': 'bdate'}
        r = requests.get(f'{API_URL}/friends.get', params=payload)
        friends = (r.json()['response']['items'])
    except (JSONDecodeError, KeyError):
        friends = None

    if not friends:
        return
    years = {}
    for friend in friends:
        bdate = friend.get('bdate')
        if not bdate or len(bdate.split('.')) != 3:
            continue
        age = datetime.date.today().year - int(bdate.split('.')[2])
        years.setdefault(age, 0)
        years[age] += 1

    return sorted(years.items(), key=lambda x: (x[1], -x[0]), reverse=True)


if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)

######################################################################################################################
# Решение задания по requests от преподавателей
######################################################################################################################
# from json.decoder import JSONDecodeError
# from datetime import datetime
# import requests
#
# ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da' \
#                '72454d235c274f1a2be5f45ee711'
# API_URL = 'https://api.vk.com/method'
# V = '5.71'
#
#
# def get_user_id(uid):
#     users_get = '{}/users.get'.format(API_URL)
#     resp = requests.get(users_get, params={
#         'access_token': ACCESS_TOKEN,
#         'user_ids': uid,
#         'v': V
#     })
#     try:
#         resp = resp.json()
#         resp = resp['response']
#         user = resp[0]
#         return user['id']
#     except (JSONDecodeError, IndexError, KeyError):
#         pass
#
#
# def get_friends(user_id):
#     friends_get = '{}/friends.get'.format(API_URL)
#     resp = requests.get(friends_get, params={
#         'access_token': ACCESS_TOKEN,
#         'user_id': user_id,
#         'fields': 'bdate',
#         'v': V
#     })
#     try:
#         resp = resp.json()
#         resp = resp['response']
#         return resp['items']
#     except (JSONDecodeError, KeyError):
#         pass
#
#
# def calc_age(uid):
#     user_id = get_user_id(uid)
#     if user_id is None:
#         return
#
#     friends = get_friends(user_id)
#     if friends is None:
#         return
#
#     years = {}
#     cur_year = datetime.now().year
#
#     for friend in friends:
#         bdate = friend.get('bdate')
#         if not bdate:
#             continue
#
#         bdate = bdate.split('.')
#         if len(bdate) != 3:
#             continue
#
#         year = int(bdate[2])
#         diff = cur_year - year
#         years.setdefault(diff, 0)
#         years[diff] += 1
#
#     return sorted(years.items(), key=lambda v: (v[1], -v[0]), reverse=True)
