import requests

# Make a Request
r = requests.get('http://httpbin.org/get')
print(r.text)
# {
#   "args": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Connection": "close",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.18.1"
#   },
#   "origin": "185.136.79.217",
#   "url": "http://httpbin.org/get"
# }

r = requests.post('http://httpbin.org/post')
print(r.text)
# {
#   "args": {},
#   "data": "",
#   "files": {},
#   "form": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Connection": "close",
#     "Content-Length": "0",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.18.1"
#   },
#   "json": null,
#   "origin": "185.136.79.217",
#   "url": "http://httpbin.org/post"
# }

# Passing Parameters
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.text)
# {
#   "args": {
#     "key1": "value1",
#     "key2": "value2"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Connection": "close",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.18.1"
#   },
#   "origin": "185.136.79.217",
#   "url": "http://httpbin.org/get?key1=value1&key2=value2"
# }

r = requests.put('http://httpbin.org/put', data={'key': 'value'})
print(r.text)
# {
#   "args": {},
#   "data": "",
#   "files": {},
#   "form": {
#     "key": "value"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Connection": "close",
#     "Content-Length": "9",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.18.1"
#   },
#   "json": null,
#   "origin": "185.136.79.217",
#   "url": "http://httpbin.org/put"
# }

import json

url = 'http://httpbin.org/post'
r = requests.post(url, data=json.dumps({'key': 'value'}))
r = requests.post(url, json={'key': 'value'})
print(r.text)
# {
#   "args": {},
#   "data": "{\"key\": \"value\"}",
#   "files": {},
#   "form": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Connection": "close",
#     "Content-Length": "16",
#     "Content-Type": "application/json",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.18.1"
#   },
#   "json": {
#     "key": "value"
#   },
#   "origin": "185.136.79.217",
#   "url": "http://httpbin.org/post"
# }

# POST a Multipart-Encoded File
url = 'http://httpbin.org/post'
files = {'file':
             ('test.txt',
              open('/Users/alexander/Desktop/test.txt',
                   'rb'))}

r = requests.post(url, files=files)
print(r.text)
# {
#   "args": {},
#   "data": "",
#   "files": {
#     "file": "test content\n"
#   },
#   "form": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Connection": "close",
#     "Content-Length": "157",
#     "Content-Type": "multipart/form-data; boundary=a6d397e696144b588e9a4aa1cff723fb",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.18.1"
#   },
#   "json": null,
#   "origin": "185.136.79.217",
#   "url": "http://httpbin.org/post"
# }

# Headers
url = 'http://httpbin.org/get'
headers = {'user-agent': 'my-app/0.0.1'}

r = requests.get(url, headers=headers)
print(r.text)
# {
#   "args": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Connection": "close",
#     "Host": "httpbin.org",
#     "User-Agent": "my-app/0.0.1"
#   },
#   "origin": "185.136.79.217",
#   "url": "http://httpbin.org/get"
# }

# Response Content
r = requests.get('http://httpbin.org/get')
print(type(r.text), r.text)
print(type(r.content), r.content)
print(type(r.json()), r.json())
# <class 'str'> {
#   "args": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Connection": "close",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.18.1"
#   },
#   "origin": "185.136.79.217",
#   "url": "http://httpbin.org/get"
# }

# <class 'bytes'> b'{\n  "args": {}, \n  "headers": {\n    "Accept": "*/*", \n    "Accept-Encoding": "gzip, deflate", \n
# "Connection": "close", \n    "Host": "httpbin.org", \n    "User-Agent": "python-requests/2.18.1"\n  }, \n
# "origin": "185.136.79.217", \n  "url": "http://httpbin.org/get"\n}\n'

# <class 'dict'> {'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Connection': 'close',
# 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.18.1'}, 'origin': '185.136.79.217',
# 'url': 'http://httpbin.org/get'}

# # Response Status Codes
print(r.status_code)
print(r.status_code == requests.codes.ok)
# 200
# True

bad_r = requests.get('http://httpbin.org/status/404')
print(bad_r.status_code)
bad_r.raise_for_status()
# 404
# ---------------------------------------------------------------------------
# HTTPError                                 Traceback (most recent call last)
# <ipython-input-14-9b812f4c5860> in <module>()
#       1 bad_r = requests.get('http://httpbin.org/status/404')
#       2 print(bad_r.status_code)
# ----> 3 bad_r.raise_for_status()
#
# /Users/alexander/Development/deep-completion/env/lib/python3.6/site-packages/requests/models.py in raise_for_status(self)
#     935
#     936         if http_error_msg:
# --> 937             raise HTTPError(http_error_msg, response=self)
#     938
#     939     def close(self):
#
# HTTPError: 404 Client Error: NOT FOUND for url: http://httpbin.org/status/404

# Response Headers
print(r.headers)

# {'Connection': 'keep-alive', 'Server': 'meinheld/0.6.1', 'Date': 'Sun, 03 Dec 2017 08:46:02 GMT',
# 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true',
# 'X-Powered-By': 'Flask', 'X-Processed-Time': '0.000767946243286', 'Content-Length': '267', 'Via': '1.1 vegur'}

# Redirection and History
r = requests.get('http://github.com')
print(r.url)
print(r.status_code)
print(r.history)
# https://github.com/
# 200
# [<Response [301]>]

r = requests.get('http://github.com', allow_redirects=False)
print(r.status_code)
print(r.history)
# 301
# []

# Cookies
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print(r.text)
# {
#   "cookies": {
#     "cookies_are": "working"
#   }
# }

# Session Objects
s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get('http://httpbin.org/cookies')
print(s.cookies)
print(r.text)
# <RequestsCookieJar[<Cookie sessioncookie=123456789 for httpbin.org/>]>
# {
#     "cookies": {
#         "sessioncookie": "123456789"
#     }
# }

s = requests.Session()
s.headers.update({'x-test': 'true'})
r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
print(r.text)
# {
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Connection": "close",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.18.1",
#     "X-Test": "true",
#     "X-Test2": "true"
#   }
# }

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