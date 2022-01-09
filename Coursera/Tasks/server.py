# # реализация сервера для тестирования метода get по заданию - Клиент для отправки метрик
# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# import socket  # для работы с сокетами используется модуль socket
#
# print('Yes')
# sock = socket.socket()  # необходимо создать сокет (данная часть является общей и для клиентских и для серверных сокетов)
# """ Теперь нужно определиться с хостом и портом для нашего сервера. Насчет хоста — если пустая строка, то наш сервер
# будет доступен для всех интерфейсов. Порт возьмем любой от нуля до 65535. В большинстве операционных систем
# прослушивание портов с номерами 0 — 1023 требует особых привилегий. Теперь свяжем наш сокет с данными хостом и портом с
# помощью метода bind, которому передается кортеж, первый элемент (или нулевой, если считать от нуля) которого — хост, а
# второй — порт"""
# sock.bind(('127.0.0.1', 8888))
# """ Теперь у нас все готово, чтобы принимать соединения. С помощью метода listen мы запустим для данного сокета режим
#  прослушивания. Метод принимает один аргумент — максимальное количество подключений в очереди."""
# sock.listen(1)
# """ Ну вот, наконец-то, мы можем принять подключение с помощью метода accept, который возвращает кортеж с двумя
#  элементами: новый сокет и адрес клиента. Именно этот сокет и будет использоваться для приема и посылке клиенту данных."""
# conn, addr = sock.accept()
#
# print('Соединение установлено:', addr)
#
# # переменная response хранит строку возвращаемую сервером, если вам для
# # тестирования клиента необходим другой ответ, измените ее
# # response = b'ok\npalm.cpu 10.5 1501864247\neardrum.cpu 15.3 1501864259\n\n'
# response = b'ok\npalm.cpu 2.0 1150864247\npalm.cpu 0.5 1150864248\neardrum.cpu 3.0 1150864250\n\n'
#
# """ Теперь мы установили с клиентом связь и можем с ним «общаться». Т.к. мы не можем точно знать, что и в каких объемах
#  клиент нам пошлет, то мы будем получать данные от него небольшими порциями. Чтобы получить данные нужно воспользоваться
#   методом recv, который в качестве аргумента принимает количество байт для чтения. Мы будем читать порциями по 1024 байт
#    (или 1 кб). для общения с клиентом мы используем сокет, который получили в результате выполнения метода accept. Мы в
#   бесконечном цикле принимаем 1024 байт данных с помощью метода recv. Если данных больше нет, то этот метод ничего не
#    возвращает. Таким образом мы можем получать от клиента любое количество данных."""
# while True:
#     data = conn.recv(1024)
#     if not data:
#         break
#     request = data.decode('utf-8')
#     print(f'Получен запрос: {ascii(request)}')
#     print(f'Отправлен ответ {ascii(response.decode("utf-8"))}')
#     conn.send(response)  # возьмем данные и отправим их клиенту
#
# conn.close()  # Теперь можно и закрыть соединение
#
#
# # Клиент
# # Думаю, что теперь будет легче. Да и само клиентское приложение проще — нам нужно создать сокет, подключиться к
# серверу, послать ему данные, принять данные и закрыть соединение. Все это делается так:
#
# #!/usr/bin/env python
# # -*- coding: utf-8 -*-
#
# # import socket
#
# # sock = socket.socket()
# # sock.connect(('localhost', 9090))
# # sock.send('hello, world!')
# #
# # data = sock.recv(1024)
# # sock.close()
# #
# # print(data)
#
# #Все понятно, т.к. все уже разбиралось ранее. Единственное новое здесь — это метод connect, с помощью которого мы
# # подключаемся к серверу. Дальше мы читаем 1024 байт данных и закрываем сокет.
#######################################################################################################################

# На предыдущей неделе вы разработали клиентское сетевое приложение — клиента для сервера метрик, который умеет
# отправлять и получать данные о различных численных показателях. Пришло время финального задания — в нем необходимо
# реализовать серверную часть.
# Как обычно, вам необходимо разработать программу в одном файле-модуле, который вы загрузите на проверку обычным
# способом. Сервер должен соответствовать протоколу, который был описан в задании к предыдущей неделе. Он должен уметь
# принимать от клиентов команды put и get, разбирать их, и формировать ответ согласно протоколу. По запросу put
# требуется сохранять метрики в структурах данных в памяти процесса. По запросу get сервер обязан отдавать данные в
# правильной последовательности. При работе с клиентом сервер должен поддерживать сессии, соединение с клиентом между
# запросами не должно "разрываться".
# На верхнем уровне вашего модуля должна быть объявлена функция run_server(host, port) — она принимает адрес и порт, на
# которых должен быть запущен сервер.
# Для проверки правильности решения мы воспользуемся своей реализацией клиента и будем отправлять на ваш сервер put и
# get запросы, ожидая в ответ правильные данные от сервера (согласно объявленному протоколу). Все запросы будут
# выполняться с таймаутом — сервер должен отвечать за приемлемое время.
# Сервер должен быть готов к неправильным командам со стороны клиента и отдавать клиенту ошибку в формате, оговоренном
# в протоколе. В этих случаях работа сервера не должна завершаться аварийно.
# На последней неделе мы с вами разбирали пример tcp-сервера на asyncio:

# import asyncio
# class ClientServerProtocol(asyncio.Protocol):
#     def connection_made(self, transport):
#         self.transport = transport
#
#     def data_received(self, data):
#         resp = process_data(data.decode())
#         self.transport.write(resp.encode())
# loop = asyncio.get_event_loop()
# coro = loop.create_server(
#     ClientServerProtocol,
#     '127.0.0.1', 8181
# )
# server = loop.run_until_complete(coro)
# try:
#     loop.run_forever()
# except KeyboardInterrupt:
#     pass
# server.close()
# loop.run_until_complete(server.wait_closed())
# loop.close()

# Данный код создает tcp-соединение для адреса 127.0.0.1:8181 и слушает все входящие запросы. При подключении клиента
# будет создан новый экземпляр класса ClientServerProtocol, а при поступлении новых данных вызовется метод этого
# объекта - data_received. Внутри asyncio.Protocol спрятана вся магия обработки запросов через корутины, остается
# реализовать протокол взаимодействия между клиентом и сервером.
# Вы можете использовать этот код, как основу при написании вашей реализации сервера. Это не обязательное требование.
# Для реализации задачи вы можете использовать любые вызовы из стандартной библиотеки Python 3 (обратим ваше внимание,
# что в грейдере установлена версия Python 3.6).  Сервер должен уметь обрабатывать запросы от нескольких клиентов
# одновременно.
# В процессе разработки сервера для тестирования работоспособности вы можете использовать клиент, написанный на
# предыдущей неделе.
# Давайте еще раз посмотрим на текстовый протокол в действии при использовании утилиты telnet:

# $: telnet 127.0.0.1 8888
# Trying 127.0.0.1...
# Connected to localhost.
# Escape character is '^]'.
# > get test_key
# < ok
# <
# > got test_key
# < error
# < wrong command
# <
# > put test_key 12.0 1503319740
# < ok
# <
# > put test_key 13.0 1503319739
# < ok
# <
# > get test_key
# < ok
# < test_key 13.0 1503319739
# < test_key 12.0 1503319740
# <
# > put another_key 10 1503319739
# < ok
# <
# > get *
# < ok
# < test_key 13.0 1503319739
# < test_key 12.0 1503319740
# < another_key 10.0 1503319739

# Также вы можете воспользоваться вспомогательным скриптом, который использует "'эталонную" реализацию клиента,
# открывающуюся после сдачи задания на пятой неделе, для локального тестирования написанного вами сервера:

# """
# Это вспомогательный скрипт для тестирования сервера из задания на неделе 6.
#
# Для запуска скрипта на локальном компьютере разместите рядом файл client.py,
# где содержится код клиента, который открывается по прохождении задания
# недели 5.
#
# Сначала запускаете ваш сервер на адресе 127.0.0.1 и порту 8888, а затем
# запускаете этот скрипт.
# """
# import sys
# from client import Client, ClientError
#
#
# def run(host, port):
#     client1 = Client(host, port, timeout=5)
#     client2 = Client(host, port, timeout=5)
#     command = "wrong command test\n"
#
#     try:
#         data = client1.get(command)
#     except ClientError:
#         pass
#     except BaseException as err:
#         print(f"Ошибка соединения с сервером: {err.__class__}: {err}")
#         sys.exit(1)
#     else:
#         print("Неверная команда, отправленная серверу, должна возвращать ошибку протокола")
#         sys.exit(1)
#
#     command = 'some_key'
#     try:
#         data_1 = client1.get(command)
#         data_2 = client1.get(command)
#     except ClientError:
#         print('Сервер вернул ответ на валидный запрос, который клиент определил, '
#               'как не корректный.. ')
#     except BaseException as err:
#         print(f"Сервер должен поддерживать соединение с клиентом между запросами, "
#               f"повторный запрос к серверу завершился ошибкой: {err.__class__}: {err}")
#         sys.exit(1)
#
#     assert data_1 == data_2 == {}, \
#         "На запрос клиента на получения данных по не существующему ключу, сервер " \
#         "вдолжен озвращать ответ с пустым полем данных."
#
#     try:
#         data_1 = client1.get(command)
#         data_2 = client2.get(command)
#     except ClientError:
#         print('Сервер вернул ответ на валидный запрос, который клиент определил'
#               ', как не корректный.. ')
#     except BaseException as err:
#         print(f"Сервер должен поддерживать соединение с несколькими клиентами: "
#               f"{err.__class__}: {err}")
#         sys.exit(1)
#
#     assert data_1 == data_2 == {}, \
#         "На запрос клиента на получения данных по не существующему ключу, сервер " \
#         "должен возвращать ответ с пустым полем данных."
#
#     try:
#         client1.put("k1", 0.25, timestamp=1)
#         client2.put("k1", 2.156, timestamp=2)
#         client1.put("k1", 0.35, timestamp=3)
#         client2.put("k2", 30, timestamp=4)
#         client1.put("k2", 40, timestamp=5)
#         client1.put("k2", 41, timestamp=5)
#     except Exception as err:
#         print(f"Ошибка вызова client.put(...) {err.__class__}: {err}")
#         sys.exit(1)
#
#     expected_metrics = {
#         "k1": [(1, 0.25), (2, 2.156), (3, 0.35)],
#         "k2": [(4, 30.0), (5, 41.0)],
#     }
#
#     try:
#         metrics = client1.get("*")
#         if metrics != expected_metrics:
#             print(f"client.get('*') вернул неверный результат. Ожидается: "
#                   f"{expected_metrics}. Получено: {metrics}")
#             sys.exit(1)
#     except Exception as err:
#         print(f"Ошибка вызова client.get('*') {err.__class__}: {err}")
#         sys.exit(1)
#
#     expected_metrics = {"k2": [(4, 30.0), (5, 41.0)]}
#
#     try:
#         metrics = client2.get("k2")
#         if metrics != expected_metrics:
#             print(f"client.get('k2') вернул неверный результат. Ожидается: "
#                   f"{expected_metrics}. Получено: {metrics}")
#             sys.exit(1)
#     except Exception as err:
#         print(f"Ошибка вызова client.get('k2') {err.__class__}: {err}")
#         sys.exit(1)
#
#     try:
#         result = client1.get("k3")
#         if result != {}:
#             print(
#                 f"Ошибка вызова метода get с ключом, который еще не был добавлен. "
#                 f"Ожидается: пустой словарь. Получено: {result}")
#             sys.exit(1)
#     except Exception as err:
#         print(f"Ошибка вызова метода get с ключом, который еще не был добавлен: "
#               f"{err.__class__} {err}")
#         sys.exit(1)
#
#     print("Похоже, что все верно! Попробуйте отправить решение на проверку.")
#
#
# if __name__ == "__main__":
#     run("127.0.0.1", 8888)

######################################################################################################################
#
# import asyncio
#
# class ClientError(Exception):
#     pass
#
# class EchoServerClientProtocol(asyncio.Protocol):
#     metrics_dict = {}
#
#     def __init__(self):
#         super().__init__()
#         self.transport = None
#         self._buffer = b''
#
#     def process_data(self, data):
#         result = 'ok\n'
#         messages = data.split("\n")
#         for command in messages:
#             if not command:
#                 continue
#             try:
#                 method, metric = command.strip().split(" ", 1)
#                 if method == "put":
#                     name, value, timestamp = metric.split()
#                     if name not in self.metrics_dict:
#                         self.metrics_dict[name] = {}
#                     self.metrics_dict[name][int(timestamp)] = float(value)
#                     return result + '\n'
#                 elif method == "get":
#                     responses, result_dict, name = [], {}, metric
#                     if len(name.strip().split(" ")) != 1:
#                         raise ValueError("wrong command")
#                     if name != "*":
#                         result_dict = {name: self.metrics_dict.get(name, {})}
#                     if name == "*":
#                         result_dict = self.metrics_dict
#                     for name in result_dict.keys():
#                         for timestamp in sorted(result_dict[name]):
#                             responses.append(
#                                 f"{name} {result_dict[name][timestamp]}"
#                                 f" {timestamp}"
#                             )
#                     if responses:
#                         result += '\n'.join(responses) + '\n'
#                     return result + '\n'
#                 else:
#                     raise ValueError("unknown method")
#             except ValueError:
#                 raise ClientError("wrong command")
#         raise ClientError("wrong command")
#
#     def connection_made(self, transport):
#         self.transport = transport
#
#     def data_received(self, data: bytes):
#         self._buffer += data
#         decoded_data = self._buffer.decode()
#         if not decoded_data.endswith('\n'):
#             return
#         self._buffer = b''
#         try:
#             resp = self.process_data(decoded_data)
#         except ClientError as err:
#             self.transport.write(f"error\n{err}\n\n".encode())
#             return
#         self.transport.write(resp.encode())
#
#
# def run_server(host, port):
#     loop = asyncio.get_event_loop()
#     coro = loop.create_server(
#         EchoServerClientProtocol,
#         host, port
#     )
#     server = loop.run_until_complete(coro)
#     try:
#         loop.run_forever()
#     except KeyboardInterrupt:
#         pass
#
#     server.close()
#     loop.run_until_complete(server.wait_closed())
#     loop.close()
#
#
# if __name__ == "__main__":
#     run_server('127.0.0.1', 8888)

######################################################################################################################
#
# import asyncio
# from collections import defaultdict
# from copy import deepcopy
#
#
# class StorageDriverError(ValueError):
#     pass
#
#
# class Storage:
#     """Класс для хранения метрик в памяти процесса"""
#
#     def __init__(self):
#         self._data = defaultdict(dict)
#
#     def put(self, key, value, timestamp):
#         self._data[key][timestamp] = value
#
#     def get(self, key):
#
#         if key == '*':
#             return deepcopy(self._data)
#
#         if key in self._data:
#             return {key: deepcopy(self._data.get(key))}
#
#         return {}
#
#
# class StorageDriver:
#     """Класс, предосталяющий интерфейс для работы с хранилищем данных"""
#
#     def __init__(self, storage):
#         self.storage = storage
#
#     def __call__(self, data):
#
#         method, *params = data.split()
#
#         if method == "put":
#             key, value, timestamp = params
#             value, timestamp = float(value), int(timestamp)
#             self.storage.put(key, value, timestamp)
#             return {}
#         elif method == "get":
#             key = params.pop()
#             if params:
#                 raise StorageDriverError
#             return self.storage.get(key)
#         else:
#             raise StorageDriverError
#
#
# class MetricsStorageServerProtocol(asyncio.Protocol):
#     """Класс для реализации сервера при помощи asyncio"""
#
#     # Обратите внимание на то, что storage является атрибутом класса, что предоставляет
#     # доступ к хранилищу данных для всех экземпляров класса MetricsStorageServerProtocol
#     # через обращение к атрибуту self.storage.
#     storage = Storage()
#     # настройки сообщений сервера
#     sep = '\n'
#     error_message = "wrong command"
#     code_err = 'error'
#     code_ok = 'ok'
#
#     def __init__(self):
#         super().__init__()
#         self.driver = StorageDriver(self.storage)
#         self._buffer = b''
#
#     def connection_made(self, transport):
#         self.transport = transport
#
#     def data_received(self, data):
#         """Метод data_received вызывается при получении данных в сокете"""
#
#         self._buffer += data
#
#         try:
#             request = self._buffer.decode()
#             # ждем данных, если команда не завершена символом \n
#             if not request.endswith(self.sep):
#                 return
#
#             self._buffer, message = b'', ''
#             raw_data = self.driver(request.rstrip(self.sep))
#
#             for key, values in raw_data.items():
#                 message += self.sep.join(f'{key} {value} {timestamp}' \
#                                          for timestamp, value in sorted(values.items()))
#                 message += self.sep
#
#             code = self.code_ok
#         except (ValueError, UnicodeDecodeError, IndexError):
#             message = self.error_message + self.sep
#             code = self.code_err
#
#         response = f'{code}{self.sep}{message}{self.sep}'
#         # отправляем ответ
#         self.transport.write(response.encode())
#
#
# def run_server(host, port):
#     loop = asyncio.get_event_loop()
#     coro = loop.create_server(MetricsStorageServerProtocol, host, port)
#     server = loop.run_until_complete(coro)
#
#     try:
#         loop.run_forever()
#     except KeyboardInterrupt:
#         pass
#
#     server.close()
#     loop.run_until_complete(server.wait_closed())
#     loop.close()
#
#
# if __name__ == "__main__":
#     run_server("127.0.0.1", 8888)

######################################################################################################################

# import asyncio
#
#
# class Storage:
#     """Класс для хранения метрик в памяти процесса"""
#
#     def __init__(self):
#         # используем словарь для хранения метрик
#         self._data = {}
#
#     def put(self, key, value, timestamp):
#         if key not in self._data:
#             self._data[key] = {}
#
#         self._data[key][timestamp] = value
#
#     def get(self, key):
#         data = self._data
#
#         # вовзращаем нужную метрику если это не *
#         if key != "*":
#             data = {
#                 key: data.get(key, {})
#             }
#
#         # для простоты мы храним метрики в обычном словаре и сортируем значения
#         # при каждом запросе, в реальном приложении следует выбрать другую
#         # структуру данных
#         result = {}
#         for key, timestamp_data in data.items():
#             result[key] = sorted(timestamp_data.items())
#
#         return result
#
#
# class ParseError(ValueError):
#     pass
#
#
# class Parser:
#     """Класс для реализации протокола"""
#
#     def encode(self, responses):
#         """Преобразование ответа сервера в строку для передачи в сокет"""
#         rows = []
#         for response in responses:
#             if not response:
#                 continue
#             for key, values in response.items():
#                 for timestamp, value in values:
#                     rows.append(f"{key} {value} {timestamp}")
#
#         result = "ok\n"
#
#         if rows:
#             result += "\n".join(rows) + "\n"
#
#         return result + "\n"
#
#     def decode(self, data):
#         """Разбор команды для дальнейшего выполнения. Возвращает список команд для выполнения"""
#         parts = data.split("\n")
#         commands = []
#         for part in parts:
#             if not part:
#                 continue
#
#             try:
#                 method, params = part.strip().split(" ", 1)
#                 if method == "put":
#                     key, value, timestamp = params.split()
#                     commands.append(
#                         (method, key, float(value), int(timestamp))
#                     )
#                 elif method == "get":
#                     key = params
#                     commands.append(
#                         (method, key)
#                     )
#                 else:
#                     raise ValueError("unknown method")
#             except ValueError:
#                 raise ParseError("wrong command")
#
#         return commands
#
#
# class ExecutorError(Exception):
#     pass
#
#
# class Executor:
#     """Класс Executor реализует метод run, который знает как выполнять команды сервера"""
#
#     def __init__(self, storage):
#         self.storage = storage
#
#     def run(self, method, *params):
#         if method == "put":
#             return self.storage.put(*params)
#         elif method == "get":
#             return self.storage.get(*params)
#         else:
#             raise ExecutorError("Unsupported method")
#
#
# class EchoServerClientProtocol(asyncio.Protocol):
#     """Класс для реализции сервера при помощи asyncio"""
#
#     # Обратите внимание на то, что storage является атрибутом класса
#     # Объект self.storage для всех экземмпляров класса EchoServerClientProtocol
#     # будет являться одним и тем же объектом для хранения метрик.
#     storage = Storage()
#
#     def __init__(self):
#         super().__init__()
#
#         self.parser = Parser()
#         self.executor = Executor(self.storage)
#         self._buffer = b''
#
#     def process_data(self, data):
#         """Обработка входной команды сервера"""
#
#         # разбираем сообщения при помощи self.parser
#         commands = self.parser.decode(data)
#
#         # выполняем команды и запоминаем результаты выполнения
#         responses = []
#         for command in commands:
#             resp = self.executor.run(*command)
#             responses.append(resp)
#
#         # преобразовываем команды в строку
#         return self.parser.encode(responses)
#
#     def connection_made(self, transport):
#         self.transport = transport
#
#     def data_received(self, data):
#         """Метод data_received вызывается при получении данных в сокете"""
#         self._buffer += data
#         try:
#             decoded_data = self._buffer.decode()
#         except UnicodeDecodeError:
#             return
#
#         # ждем данных, если команда не завершена символом \n
#         if not decoded_data.endswith('\n'):
#             return
#
#         self._buffer = b''
#
#         try:
#             # обрабатываем поступивший запрос
#             resp = self.process_data(decoded_data)
#         except (ParseError, ExecutorError) as err:
#             # формируем ошибку, в случае ожидаемых исключений
#             self.transport.write(f"error\n{err}\n\n".encode())
#             return
#
#         # формируем успешный ответ
#         self.transport.write(resp.encode())
#
#
# def run_server(host, port):
#     loop = asyncio.get_event_loop()
#     coro = loop.create_server(
#         EchoServerClientProtocol,
#         host, port
#     )
#     server = loop.run_until_complete(coro)
#     try:
#         loop.run_forever()
#     except KeyboardInterrupt:
#         pass
#
#     server.close()
#     loop.run_until_complete(server.wait_closed())
#     loop.close()
#
#
# if __name__ == "__main__":
#     # запуск сервера для тестирования
#     run_server('127.0.0.1', 8888)

######################################################################################################################
