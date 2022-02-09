from bs4 import BeautifulSoup
# import unittest
import os
import re

# graph = {'A': ['B', 'C'],
#          'B': ['C', 'D'],
#          'C': ['D'],
#          'D': ['C'],
#          'E': ['F'],
#          'F': ['C']}
#
#
# def find_shortest_path(graph, start, end, path=[]):
#     path = path + [start]
#     if start == end:
#         return path
#     # if not graph.has_key(start):
#     #     return None
#     shortest = None
#     for node in graph[start]:
#         if node not in path:
#             newpath = find_shortest_path(graph, node, end, path)
#             if newpath:
#                 if not shortest or len(newpath) < len(shortest):
#                     shortest = newpath
#     return shortest
#
# print(find_shortest_path(graph, 'A', 'D'))

start = 'Stone_Age'
end = 'Python_(programming_language)'
path = './wiki/'
files = dict.fromkeys(os.listdir('./wiki/'))  # Словарь вида {"filename1": None, "filename2": None, ...}
print(files)
link_list = [start]
while link_list:
    for id, link in enumerate(link_list):
        with open("{}{}".format(path, link), encoding='utf-8') as data:
            file_links = link_re.findall(data.read())
            for lnk in [i for i in file_links if i in files.keys()]:
                if files.get(lnk) is None:
                    files[lnk] = link
                    if lnk == end:
                        print(files)
                    link_list.append(lnk)
        link_list.pop(id)



# path = "wiki/Stone_Age"
# # path = './wiki/'  os.path.join('wiki', file)
# # for file in os.listdir(path):
#     # print(file)
# with open(path, encoding='utf-8') as data:
#     soup = BeautifulSoup(data, "lxml")
#
# body = soup.find(id="bodyContent")
# # print(body)
#
# imgs = len((body.find_all('img', width=lambda x: int(x or 0) > 199)))
#
#
# headers = 10  # Количество заголовков, первая буква текста внутри которого: E, T или C
# # headers = len([i.text for i in body.find_all(name=re.compile(r'[hH1-6]{2}')) if i.text[0] in 'ETC'])
#
# # linkslen = 15  # Длина максимальной последовательности ссылок, между которыми нет других тегов
# linkslen = 0
# link_found = body.find_next('a')
# while link_found:
#     local_linklen = 1
#     for i in link_found.find_next_siblings():
#         if i.name == 'a':
#             local_linklen += 1
#         else:
#             break
#     linkslen = max(linkslen, local_linklen)
#     link_found = link_found.find_next('a')
#
# # lists = 20  # Количество списков, не вложенных в другие списки
# lists = 0
# html_lists = body.find_all(['ul', 'ol'])
# for html_list in html_lists:
#     if not html_list.find_parents(['ul', 'ol']):
#         lists += 1
#
# out = [imgs, headers, linkslen, lists]
# print(out)

# import os
#
# fds = sorted(os.listdir('/home/username/Images/'))
#
# for img in fds:
#     if img.endswith(('.jpg', '.png')): # если имя оканчивается на что-то из tuple...
#         print(img) # выводим имя файла


#########################################################################################
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
# #################################################################################################
