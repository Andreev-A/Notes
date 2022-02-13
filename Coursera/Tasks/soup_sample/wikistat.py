# Часть 1:
# В этом задании вам необходимо реализовать парсер для сбора статистики со страниц Википедии. Чтобы упростить вашу
# задачу, необходимые страницы уже скачаны и сохранены на файловой системе в директории wiki/ (Например, страница
# https://en.wikipedia.org/wiki/Stone_Age сохранена файле wiki/Stone_Age).
# Парсер реализован в виде функции parse, которая принимает на вход один параметр: path_to_file — путь до файла,
# содержащий html код страницы википедии. Гарантируется, что такой путь существует. Ваша задача — прочитать файл,
# пройтись Beautiful Soup по статье, найти её тело (это <div id="bodyContent">) и внутри него подсчитать:
# Количество картинок (img) с шириной (width) не меньше 200. Например: <img width="200">, но не <img> и не
# <img width="199">
# Количество заголовков (h1, h2, h3, h4, h5, h6), первая буква текста внутри которых соответствует заглавной букве
# E, T или C. Например: <h1>End</h1> или <h5><span>Contents</span></h5>, но не <h1>About</h1> и не <h2>end</h2> и не
# <h3><span>1</span><span>End</span></h3>
# Длину максимальной последовательности ссылок, между которыми нет других тегов, открывающихся или закрывающихся.
# Например: <p><span><a></a></span>, <a></a>, <a></a></p> - тут 2 ссылки подряд, т.к. закрывающийся span прерывает
# последовательность. <p><a><span></span></a>, <a></a>, <a></a></p> - а тут 3 ссылки подряд, т.к. span находится внутри
# ссылки, а не между ссылками.
# Количество списков (ul, ol), не вложенных в другие списки. Например: <ol><li></li></ol>,
# <ul><li><ol><li></li></ol></li></ul> - два не вложенных списка (и один вложенный)
# Результатом работы функции parse будет список четырех чисел, посчитанных по формулам выше.
# В пункте про последовательность ссылок вы можете ошибиться с результатом, если решите использовать метод find_next().
# Обратите внимание, что хотя find_next находит тег, идущий сразу за текущим, этот тег может оказаться вложенным в
# текущий, а не быть его следующим соседом. Возможно, нужно использовать другой метод или алгоритм.
# Так же, не упустите момент, что данные во всех пунктах нужно искать внутри <div id="bodyContent">, а не по всей
# странице.


from bs4 import BeautifulSoup
import unittest
import re


def parse(path_to_file):
    with open(path_to_file, encoding='utf-8') as data:
        soup = BeautifulSoup(data, 'html.parser')
    body = soup.find(id="bodyContent")

    imgs = len((body.find_all('img', width=lambda x: int(x or 0) > 199)))

    headers = len([i.text for i in body.find_all(name=re.compile(r'[hH1-6]{2}')) if i.text[0] in 'ETC'])

    linkslen = 0
    all_links = body.find_all('a')
    for link in all_links:
        current_count = 1
        siblings = link.find_next_siblings()
        for sibling in siblings:
            if sibling.name == 'a':
                current_count += 1
                linkslen = max(current_count, linkslen)
            else:
                current_count = 0

    lists = 0
    html_lists = body.find_all(['ul', 'ol'])
    for html_list in html_lists:
        if not html_list.find_parents(['ul', 'ol']):
            lists += 1

    return [imgs, headers, linkslen, lists]


class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ('wiki/Stone_Age', [13, 10, 12, 40]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
            ('wiki/Spectrogram', [1, 2, 4, 7]),)

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


if __name__ == '__main__':
    unittest.main()

######################################################################################################################
# 2 часть
######################################################################################################################
# Часть 2:
# В этом задании продолжаем работать со страницами из wikipedia. Необходимо реализовать механизм сбора статистики по
# нескольким страницам. Сложность задачи состоит в том, что сначала нужно будет определить страницы, с которых
# необходимо собирать статистику. В качестве входных данных служат названия двух статей(страниц). Гарантируется, что
# файлы обеих статей есть в папке wiki и из первой статьи можно попасть в последнюю, переходя по ссылкам только на те
# статьи, копии которых есть в папке wiki.
# Например, на вход подаются страницы: Stone_Age и Python_(programming_language). В статье Stone_Age есть ссылка на
# Brain, в ней на Artificial_intelligence, а в ней на Python_(programming_language) и это кратчайший путь от Stone_Age
# до Python_(programming_language). Ваша задача — найти самый короткий путь (гарантируется, что существует только один
# путь минимальной длины), а затем с помощью функции parse из предыдущего задания собрать статистику по всем статьям в
# найденном пути.
# Результат нужно вернуть в виде словаря, ключами которого являются имена статей, а значениями списки со статистикой.
# Для нашего примера правильный результат будет :
# { 'Stone_Age': [13, 10, 12, 40],
#   'Brain': [19, 5, 25, 11],
#   'Artificial_intelligence': [8, 19, 13, 198],
#   'Python_(programming_language)': [2, 5, 17, 41]
# }
# Вам необходимо реализовать две функции:  build_bridge и get_statistics.
# def build_bridge(path, start_page, end_page):
#     """возвращает список страниц, по которым можно перейти по ссылкам со start_page на
#     end_page, начальная и конечная страницы включаются в результирующий список"""
#
#     # напишите вашу реализацию логики по вычисления кратчайшего пути здесь
#
#
# def get_statistics(path, start_page, end_page):
#     """собирает статистику со страниц, возвращает словарь, где ключ - название страницы,
#     значение - список со статистикой страницы"""
#
#     # получаем список страниц, с которых необходимо собрать статистику
#     pages = build_bridge(path, start_page, end_page)
#     # напишите вашу реализацию логики по сбору статистики здесь
#
#     return statistic
# Обе функции принимают на вход три параметра:path - путь до директории с сохраненными файлами из wikipedia,start_page
# - название начальной страницы,end_page - название конечной страницы.
# Функция build_bridge вычисляет кратчайший путь и возвращает список страниц в том порядке, в котором происходят
# переходы. Начальная и конечная страницы включаются в результирующий список. В случае, если название стартовой и
# конечной страницы совпадают, то результирующий список должен содержать только стартовую страницу. Получить все ссылки
# на странице можно разными способами, в том числе и с помощью регулярных выражений, например так:
# with open(os.path.join(path, page), encoding="utf-8") as file:
#     links = re.findall(r"(?<=/wiki/)[\w()]+", file.read())
# Обратите внимание, что что на страницах wikipedia могут встречаться ссылки на страницы, которых нет в директории wiki,
# такие ссылки должны игнорироваться.
# Пример работы функции build_bridge:
# >>> result = build_bridge('wiki/', 'The_New_York_Times', 'Stone_Age')
# >>> print(result)
# ['The_New_York_Times', 'London', 'Woolwich', 'Iron_Age', 'Stone_Age']
# Функция get_statistics использует функцию parse и собирает статистику по страницам, найденным с помощью функции
# build_bridge. Пример работы функции get_statistics:
# >>> from pprint import pprint
# >>> result = get_statistics('wiki/', 'The_New_York_Times', "Binyamina_train_station_suicide_bombing")
# >>> pprint(result)
# {'Binyamina_train_station_suicide_bombing': [1, 3, 6, 21],
#  'Haifa_bus_16_suicide_bombing': [1, 4, 15, 23],
#  'Second_Intifada': [9, 13, 14, 84],
#  'The_New_York_Times': [5, 9, 8, 42]}
# Вы можете использовать для проверки вашего решения тесты:
# Набор тестов для проверки студентами решений по заданию "Практическое задание
# по Beautiful Soup - 2". По умолчанию файл с решением называется solution.py,
# измените в импорте название модуля solution, если файл с решением имеет другое имя.

# import unittest
# from solution import build_bridge, get_statistics
#
# STATISTICS = {
#     'Artificial_intelligence': [8, 19, 13, 198],
#     'Binyamina_train_station_suicide_bombing': [1, 3, 6, 21],
#     'Brain': [19, 5, 25, 11],
#     'Haifa_bus_16_suicide_bombing': [1, 4, 15, 23],
#     'Hidamari_no_Ki': [1, 5, 5, 35],
#     'IBM': [13, 3, 21, 33],
#     'Iron_Age': [4, 8, 15, 22],
#     'London': [53, 16, 31, 125],
#     'Mei_Kurokawa': [1, 1, 2, 7],
#     'PlayStation_3': [13, 5, 14, 148],
#     'Python_(programming_language)': [2, 5, 17, 41],
#     'Second_Intifada': [9, 13, 14, 84],
#     'Stone_Age': [13, 10, 12, 40],
#     'The_New_York_Times': [5, 9, 8, 42],
#     'Wild_Arms_(video_game)': [3, 3, 10, 27],
#     'Woolwich': [15, 9, 19, 38]}
#
# TESTCASES = (
#     ('wiki/', 'Stone_Age', 'Python_(programming_language)',
#      ['Stone_Age', 'Brain', 'Artificial_intelligence', 'Python_(programming_language)']),
#
#     ('wiki/', 'The_New_York_Times', 'Stone_Age',
#      ['The_New_York_Times', 'London', 'Woolwich', 'Iron_Age', 'Stone_Age']),
#
#     ('wiki/', 'Artificial_intelligence', 'Mei_Kurokawa',
#      ['Artificial_intelligence', 'IBM', 'PlayStation_3', 'Wild_Arms_(video_game)',
#       'Hidamari_no_Ki', 'Mei_Kurokawa']),
#
#     ('wiki/', 'The_New_York_Times', "Binyamina_train_station_suicide_bombing",
#      ['The_New_York_Times', 'Second_Intifada', 'Haifa_bus_16_suicide_bombing',
#       'Binyamina_train_station_suicide_bombing']),
#
#     ('wiki/', 'Stone_Age', 'Stone_Age',
#      ['Stone_Age', ]),
# )
#
#
# class TestBuildBrige(unittest.TestCase):
#     def test_build_bridge(self):
#         for path, start_page, end_page, expected in TESTCASES:
#             with self.subTest(path=path,
#                               start_page=start_page,
#                               end_page=end_page,
#                               expected=expected):
#                 result = build_bridge(path, start_page, end_page)
#                 self.assertEqual(result, expected)
#
#
# class TestGetStatistics(unittest.TestCase):
#     def test_build_bridge(self):
#         for path, start_page, end_page, expected in TESTCASES:
#             with self.subTest(path=path,
#                               start_page=start_page,
#                               end_page=end_page,
#                               expected=expected):
#                 result = get_statistics(path, start_page, end_page)
#                 self.assertEqual(result, {page: STATISTICS[page] for page in expected})
#
#
# if __name__ == '__main__':
#     unittest.main()

import os
import re
from bs4 import BeautifulSoup


def get_backlinks(path, end_page, unchecked_pages, checked_pages, backlinks):
    if end_page in checked_pages or not checked_pages:
        return backlinks

    new_checked_pages = set()

    for checked_page in checked_pages:
        unchecked_pages.remove(checked_page)
        with open(os.path.join(path, checked_page), encoding="utf-8") as file:
            links = set(re.findall(r"(?<=/wiki/)[\w()]+", file.read()))
            if checked_page in links:
                links.remove(checked_page)
        linked_pages = links & unchecked_pages

        for linked_page in linked_pages:
            backlinks[linked_page] = backlinks.get(linked_page, checked_page)
            new_checked_pages.add(linked_page)

    checked_pages = new_checked_pages & unchecked_pages

    return get_backlinks(path, end_page, unchecked_pages, checked_pages, backlinks)


def build_bridge(path, start_page, end_page):
    backlinks = \
        get_backlinks(path, end_page, set(os.listdir(path)), {start_page, }, dict())

    current_page, bridge = end_page, [end_page]

    while current_page != start_page:
        current_page = backlinks.get(current_page)
        bridge.append(current_page)

    return bridge[::-1]


def get_statistics(path, start_page, end_page):
    pages = build_bridge(path, start_page, end_page)
    statistic = {}
    for file in pages:
        with open("{}{}".format(path, file), encoding='utf-8') as data:
            soup = BeautifulSoup(data, 'html.parser')
        body = soup.find(id="bodyContent")

        imgs = len((body.find_all('img', width=lambda x: int(x or 0) > 199)))

        headers = len([i.text for i in body.find_all(name=re.compile(r'[hH1-6]{2}')) if i.text[0] in 'ETC'])

        linkslen = 0
        all_links = body.find_all('a')
        for link in all_links:
            current_count = 1
            siblings = link.find_next_siblings()
            for sibling in siblings:
                if sibling.name == 'a':
                    current_count += 1
                    linkslen = max(current_count, linkslen)
                else:
                    current_count = 0

        lists = 0
        html_lists = body.find_all(['ul', 'ol'])
        for html_list in html_lists:
            if not html_list.find_parents(['ul', 'ol']):
                lists += 1

        statistic[file] = [imgs, headers, linkslen, lists]

    return statistic
######################################################################################################################
# Решение задания по Beautiful Soup
######################################################################################################################
import unittest

from bs4 import BeautifulSoup


def parse(path_to_file):
    with open(path_to_file, encoding="utf-8") as file:
        soup = BeautifulSoup(file, "lxml")
        body = soup.find(id="bodyContent")

    # количество картинок (img) с шириной (width) не меньше 200
    imgs = len(body.find_all('img', width=lambda x: int(x or 0) > 199))

    # количество заголовков (h1, h2, h3, h4, h5, h6), первая буква текста внутри которых
    # соответствует заглавной букве E, T или C
    headers = sum(1 for tag in body.find_all(
        ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']) if tag.get_text()[0] in "ETC")

    # количество списков (ul, ol), не вложенных в другие списки
    lists = sum(
        1 for tag in body.find_all(['ol', 'ul']) if not tag.find_parent(['ol', 'ul']))

    # Длину максимальной последовательности ссылок, между которыми нет других тегов
    linkslen = 0

    for a in body.find_all('a'):
        current_streak = 1

        for tag in a.find_next_siblings():
            if tag.name == 'a':
                current_streak += 1
            else:
                break

        linkslen = current_streak if current_streak > linkslen else linkslen

    return [imgs, headers, linkslen, lists]


class TestParse(unittest.TestCase):
    def test_parse(self):
        test_cases = (
            ('wiki/Stone_Age', [13, 10, 12, 40]),
            ('wiki/Brain', [19, 5, 25, 11]),
            ('wiki/Artificial_intelligence', [8, 19, 13, 198]),
            ('wiki/Python_(programming_language)', [2, 5, 17, 41]),
            ('wiki/Spectrogram', [1, 2, 4, 7]),)

        for path, expected in test_cases:
            with self.subTest(path=path, expected=expected):
                self.assertEqual(parse(path), expected)


if __name__ == '__main__':
    unittest.main()

#######################################################################################################################
import os
import re

from bs4 import BeautifulSoup


def parse(path_to_file):
    with open(path_to_file, encoding="utf-8") as file:
        soup = BeautifulSoup(file, "lxml")
        body = soup.find(id="bodyContent")

    imgs = len(body.find_all('img', width=lambda x: int(x or 0) > 199))

    headers = sum(1 for tag in body.find_all(
        ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']) if tag.get_text()[0] in "ETC")

    lists = sum(
        1 for tag in body.find_all(['ol', 'ul']) if not tag.find_parent(['ol', 'ul']))

    linkslen = 0

    for a in body.find_all('a'):
        current_streak = 1

        for tag in a.find_next_siblings():
            if tag.name == 'a':
                current_streak += 1
            else:
                break

        linkslen = current_streak if current_streak > linkslen else linkslen

    return [imgs, headers, linkslen, lists]


def get_statistics(path, start_page, end_page):
    """собирает статистику со страниц, возвращает словарь, где ключ - название страницы,
    значение - список со статистикой страницы"""
    pages = build_bridge(path, start_page, end_page)
    statistic = {}

    for page in pages:
        statistic[page] = parse(os.path.join(path, page))

    return statistic


def get_links(path, page):
    """возвращает множество названий страниц, ссылки на которые содержатся в файле page"""

    with open(os.path.join(path, page), encoding="utf-8") as file:
        links = set(re.findall(r"(?<=/wiki/)[\w()]+", file.read()))
        if page in links:
            links.remove(page)
    return links


def get_backlinks(path, end_page, unchecked_pages, checked_pages, backlinks):
    """возвращает словарь обратных ссылок (ключ - страница, значение - страница
    с которой возможен переход по ссылке на страницу, указанную в ключе)"""

    if end_page in checked_pages or not checked_pages:
        return backlinks

    new_checked_pages = set()

    for checked_page in checked_pages:
        unchecked_pages.remove(checked_page)
        linked_pages = get_links(path, checked_page) & unchecked_pages

        for linked_page in linked_pages:
            backlinks[linked_page] = backlinks.get(linked_page, checked_page)
            new_checked_pages.add(linked_page)

    checked_pages = new_checked_pages & unchecked_pages

    return get_backlinks(path, end_page, unchecked_pages, checked_pages, backlinks)


def build_bridge(path, start_page, end_page):
    """возвращает список страниц, по которым можно перейти по ссылкам со start_page на
    end_page, начальная и конечная страницы включаются в результирующий список"""

    backlinks = \
        get_backlinks(path, end_page, set(os.listdir(path)), {start_page, }, dict())

    current_page, bridge = end_page, [end_page]

    while current_page != start_page:
        current_page = backlinks.get(current_page)
        bridge.append(current_page)

    return bridge[::-1]

######################################################################################################################
# from bs4 import BeautifulSoup
# import requests

# resp = requests.get('https://www.wikipedia.org')
# html = resp.text

# import re
# re_links = re.findall(r'<a[^>]+class="[^"]*other-project-link[^>]+href="([^"]+)', html)
# print(re_links)

# soup = BeautifulSoup(html, 'lxml')
# bs_links = soup('a', 'other-project-link')
# bs_hrefs = [link['href'] for link in bs_links]
# print(bs_hrefs)

# html = """<!DOCTYPE html>
# <html lang="en">
# <head>
# <title>test page</title>
# </head>
# <body class="mybody" id="js-body">
# <p class="text odd">first <b>bold</b> paragraph</p>
# <p class="text even">second <a href="https://mail.ru">link</a></p>
# <p class="list odd">third <a id="paragraph"><b>bold link</b></a></p>
# </body>
# </html>
# """
# soup = BeautifulSoup(html, 'lxml')
# print(soup.head)
# print(soup)  # напечатать
# print(soup.prettify())  # красиво напечатать с отступами
# print(soup.p.b.string)  # можно .p или .p.b или p.b.string
# print(soup.p.name)  # p
# print(soup.p['class'])  # ['title'] - список, т.к. может быть много значений
# print(soup('p')[1]['class'])  # следующий класс
# print(soup.p.b.parrent)  # родитель тега b
# print(soup.p.b.parrents)  # все родители тега b - это генератор -> (вывести) [tag.name for tag in soup.p.b.parrents]
# print(soup.p.next)  # Перейти к тегу или строке непосредственно идущему за первым <p>, включая вложеный
# print(soup.p.next_sibling)  # следующий тег, не включая вложеный - у нас перенос строки (еще добавить - .next_sibling)
# print(soup.p.contents)  # все вложеные теги
# print(soup.p.children)  # все вложеные теги - генератор -> (вывести) list(soup.p.children)
#
########################################################################################################
# from bs4 import BeautifulSoup
# import re
# import os
#
#
# def get_href_page_names(page_name, wiki_path):
#     try:
#         with open(os.path.join(wiki_path, page_name)) as file:
#             html = file.read()
#             soup = BeautifulSoup(html, 'html.parser')
#             raw_a = soup.find_all('a', href=True)
#             pages_names = [
#                 x['href'].split('/')[-1]
#                 for x in raw_a
#                 if x['href'].startswith('/wiki')
#             ]
#             return pages_names
#     except FileNotFoundError:
#         return []
#
#
# def bfs_paths(start, goal, wiki_path):
#     queue = [(start, [start])]
#     while queue:
#         (vertex, path) = queue.pop(0)
#         for next in set(get_href_page_names(vertex, wiki_path)) - set(path):
#             if next == goal:
#                 yield path + [next]
#             else:
#                 queue.append((next, path + [next]))
#
#
# def shortest_path(start, goal, wiki_path):
#     try:
#         return next(bfs_paths(start, goal, wiki_path))
#     except StopIteration:
#         return None
#
#
# def get_images_amount(body):
#     imgs = body.find_all('img')
#     fit_imgs = len(
#         [x for x in imgs if x.get('width') and int(x.get('width')) >= 200]
#     )
#     return fit_imgs
#
#
# def get_headers_amount(body):
#     headers = body.find_all(re.compile('^h[1-6]$'))
#     count = 0
#     for header in headers:
#         children = header.find_all(recursive=False)
#         if children:
#             children_content = [x.getText() for x in children if x.getText()]
#             try:
#                 first_letter = children_content[0][0]
#                 if first_letter in 'ETC':
#                     count += 1
#             except IndexError:
#                 pass
#         else:
#             try:
#                 first_letter = header.getText()[0]
#                 if first_letter in 'ETC':
#                     count += 1
#             except IndexError:
#                 pass
#     return count
#
#
# def get_max_links_len(body):
#     max_count = 0
#     all_links = body.find_all('a')
#     for link in all_links:
#         current_count = 1
#         siblings = link.find_next_siblings()
#         for sibling in siblings:
#             if sibling.name == 'a':
#                 current_count += 1
#                 max_count = max(current_count, max_count)
#             else:
#                 current_count = 0
#     return max_count
#
#
# def get_lists_num(body):
#     count = 0
#     all_lists = body.find_all(['ul', 'ol'])
#     for tag in all_lists:
#         if not tag.find_parents(['ul', 'ol']):
#             count += 1
#     return count
#
#
# def parse(start, end, wiki_path):
#     bridge = shortest_path(start, end, wiki_path)
#     out = {}
#     for file in bridge:
#         with open(os.path.join(wiki_path, file)) as data:
#             soup = BeautifulSoup(data, "html.parser")
#         body = soup.find(id="bodyContent")
#
#         imgs = get_images_amount(body)
#         headers = get_headers_amount(body)
#         linkslen = get_max_links_len(body)
#         lists = get_lists_num(body)
#         out[file] = [imgs, headers, linkslen, lists]
#     return out

#########################################################################################
# from bs4 import BeautifulSoup
# import re
# import os
#
#
# # Вспомогательная функция, её наличие не обязательно и не будет проверяться
# def build_tree(start, end, path):
#     link_re = re.compile(r"(?<=/wiki/)[\w()]+")  # Искать ссылки можно как угодно, не обязательно через re
#     files = dict.fromkeys(os.listdir(path))  # Словарь вида {"filename1": None, "filename2": None, ...}
#     # TODO Проставить всем ключам в files правильного родителя в значение, начиная от start
#     link_list = [start]
#     while link_list:
#         for id, link in enumerate(link_list):
#             with open("{}{}".format(path, link), encoding='utf-8') as data:
#                 file_links = link_re.findall(data.read())
#                 for lnk in [i for i in file_links if i in files.keys()]:
#                     if files.get(lnk) is None:
#                         files[lnk] = link
#                         if lnk == end:
#                             return files
#                         link_list.append(lnk)
#             link_list.pop(id)
#     return files
#
#
# # Вспомогательная функция, её наличие не обязательно и не будет проверяться
# def build_bridge(start, end, path):
#     files = build_tree(start, end, path)
#     # TODO Добавить нужные страницы в bridge
#     parent = end
#     bridge = [parent]
#     while parent != start:
#         parent = files[parent]
#         if parent is not None:
#             bridge.append(parent)
#         else:
#             bridge.append(start)
#             parent = start
#     return bridge[::-1]
#
#
# def parse(start, end, path):
#     """
#     Если не получается найти список страниц bridge, через ссылки на которых можно добраться от start до end, то,
#     по крайней мере, известны сами start и end, и можно распарсить хотя бы их: bridge = [end, start]. Оценка за тест,
#     в этом случае, будет сильно снижена, но на минимальный проходной балл наберется, и тест будет пройден.
#     Чтобы получить максимальный балл, придется искать все страницы. Удачи!
#     """
#
#     bridge = build_bridge(start, end, path)  # Искать список страниц можно как угодно, даже так: bridge = [end, start]
#     # Когда есть список страниц, из них нужно вытащить данные и вернуть их
#     out = {}
#     for file in bridge:
#         with open("{}{}".format(path, file), encoding='utf-8') as data:
#             soup = BeautifulSoup(data, "lxml")
#
#         body = soup.find(id="bodyContent")
#
#         # TODO посчитать реальные значения
#         # imgs = 5  # Количество картинок (img) с шириной (width) не меньше 200
#         imgs = len((body.find_all('img', width=lambda x: int(x or 0) > 199)))
#
#         # headers = 10  # Количество заголовков, первая буква текста внутри которого: E, T или C
#         headers = len([i.text for i in body.find_all(name=re.compile(r'[hH1-6]{2}')) if i.text[0] in 'ETC'])
#
#         # linkslen = 15  # Длина максимальной последовательности ссылок, между которыми нет других тегов
#         linkslen = 0
#         link_found = body.find_next('a')
#         while link_found:
#             local_linklen = 1
#             for i in link_found.find_next_siblings():
#                 if i.name == 'a':
#                     local_linklen += 1
#                 else:
#                     break
#             linkslen = max(linkslen, local_linklen)
#             link_found = link_found.find_next('a')
#
#         # lists = 20  # Количество списков, не вложенных в другие списки
#         lists = 0
#         html_lists = body.find_all(['ul', 'ol'])
#         for html_list in html_lists:
#             if not html_list.find_parents(['ul', 'ol']):
#                 lists += 1
#
#         out[file] = [imgs, headers, linkslen, lists]
#
#     return out
#
#
# if __name__ == '__main__':
#     correct = {
#         'Stone_Age': [13, 10, 12, 40],
#         'Brain': [19, 5, 25, 11],
#         'Artificial_intelligence': [8, 19, 13, 198],
#         'Python_(programming_language)': [2, 5, 17, 41],
#     }
#     start = 'Stone_Age'
#     end = 'Python_(programming_language)'
#     path = './wiki/'
#
#     print('parse result:', parse(start, end, path))
#     print('correct result', correct)
#
# #####################################################################################
# from bs4 import BeautifulSoup
# import re
# import os
#
#
# def searcher(start, end, path, files, max_deep, now_deep, arr_searched):
#     now_deep += 1
#     if now_deep <= max_deep:
#         if start in arr_searched:
#             return None
#         else:
#
#             arr_searched.append(start)
#             with open(os.path.join(path, start), 'rb') as f:
#                 html = f.read()
#                 soap = BeautifulSoup(html, 'lxml')
#                 tags = soap.find_all('a', href=True)
#                 tags_true = [tag['href'].split('/wiki/')[1] for tag in tags if '/wiki/' in tag['href']]
#                 if end in tags_true:
#                     return [end]
#
#                 for tag in tags_true:
#                     if tag in files:
#                         solution = searcher(tag, end, path, files, max_deep, now_deep, arr_searched)
#                         if solution is not None:
#                             solution.append(tag)
#                             return solution
#
#     return None
#
#
# # Вспомогательная функция, её наличие не обязательно и не будет проверяться
# def build_tree(start, end, path):
#     # link_re = re.compile(r"(?<=/wiki/)[\w()]+")  # Искать ссылки можно как угодно, не обязательно через re
#     files = dict.fromkeys(os.listdir(path))  # Словарь вида {"filename1": None, "filename2": None, ...}
#     solution = None
#     for i in range(1, 20):
#         solution = searcher(start, end, path, files, i, 0, [])
#         if solution is not None:
#             return solution
#     # TODO Проставить всем ключам в files правильного родителя в значение, начиная от start
#     return solution or 0
#
#
# # Вспомогательная функция, её наличие не обязательно и не будет проверяться
# def build_bridge(start, end, path):
#     final_arr = build_tree(start, end, path)
#     final_arr.append(start)
#     return final_arr
#
#
# def parse(start, end, path):
#     """
#     Если не получается найти список страниц bridge, через ссылки на которых можно добраться от start до end, то,
#     по крайней мере, известны сами start и end, и можно распарсить хотя бы их: bridge = [end, start]. Оценка за тест,
#     в этом случае, будет сильно снижена, но на минимальный проходной балл наберется, и тест будет пройден.
#     Чтобы получить максимальный балл, придется искать все страницы. Удачи!
#     """
#
#     bridge = build_bridge(start, end, path)  # Искать список страниц можно как угодно, даже так: bridge = [end, start]
#
#     # Когда есть список страниц, из них нужно вытащить данные и вернуть их
#     out = {}
#     for file in bridge:
#         with open(os.path.join(path, file), 'rb') as data:
#             soup = BeautifulSoup(data, "lxml")
#
#         body = soup.find(id="bodyContent")
#         imgs = 0
#         for img in body.find_all('img', width=True):
#             if int(img['width']) >= 200:
#                 imgs += 1
#
#         headers = 0
#         for a in ["h1", "h2", "h3", "h4", "h5", "h6"]:
#             for head in body.find_all(a):
#                 if re.match(r'^[E,T,C]', head.text) is not None:
#                     headers += 1
#
#         linkslen = 0
#         for a in body.find_all('a'):
#             a_siblings = a.find_next_siblings()
#             len_arr = 1
#             for sib in a_siblings:
#                     if sib.name == 'a':
#                         len_arr+=1
#                     else:
#                         break
#             if len_arr > linkslen:
#                 linkslen = len_arr
#
#         lists = 0
#         for ul in body.find_all('ul'):
#             if ul.parent.name == 'div':
#                 lists += 1
#         for ol in body.find_all('ol'):
#             if ol.parent.name == 'div':
#                 lists += 1
#
#
#
#
#
#         # TODO посчитать реальные значения
#         # imgs = 5  # Количество картинок (img) с шириной (width) не меньше 200
#         # headers = 10  # Количество заголовков, первая буква текста внутри которого: E, T или C
#         # linkslen = 15  # Длина максимальной последовательности ссылок, между которыми нет других тегов
#         # lists = 20  # Количество списков, не вложенных в другие списки
#
#         out[file] = [imgs, headers, linkslen, lists]
#
#     return out
#
#
# if __name__ == '__main__':
#     print(parse('Stone_Age', 'Brain', './wiki/'))