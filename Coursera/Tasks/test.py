# Запросы клиента.
# Строка запроса в этом случае будет иметь вид:
# 1   put palm.cpu 23.7 1150864247\n
# В запросе на сохранение мы можем передать данные только об одном измерении.
# Чтобы получить с сервера данные, сохраненные по ключу «palm.cpu», необходимо в данных запроса просто передать имя
# ключа:
# 1   get palm.cpu\n
# Для случая, когда необходимо получить все хранимые на сервере данные, в качестве ключа используется символ звездочки
# «*». Пример строки запроса:
# 1  # get *\n
# Ответы сервера.
# Допустим, что на сервере хранятся данные:
#  name          | value | timestamp
# -----------------------------------
# "palm.cpu"    |  2.0  | 1150864247
# "palm.cpu"    |  0.5  | 1150864248
# "eardrum.cpu" |  3.0  | 1150864250
# Тогда в ответ на запрос о получении данных по ключу "palm.cpu" сервер отправит строку:
# 1  ok\npalm.cpu 2.0 1150864247\npalm.cpu 0.5 1150864248\n\n
# Строка ответа сервера на запрос о получении всех хранящихся на сервере данных (в качестве ключа передано «*») в нашем
# случае будет таким:
# 1  # ok\npalm.cpu 2.0 1150864247\npalm.cpu 0.5 1150864248\neardrum.cpu 3.0 1150864250\n\n
# В случаях:
# - когда в запросе на получение данных передан не существующий ключ
# - успешного выполнения команды сохранения данных put
# сервер отправляет клиенту строку со статусом «оk» и пустым полем с данными ответа:
# 1   ok\n\n
# Если в параметре запроса переданы не валидные данные (например: нарушен формат запроса, ошибочная команда или значения
# value и timestamp не могут быть приведены к необходимому типу данных) сервер отправляет строку со статусом ответа
# «error» и данными ответа «wrong command»:
# 1   error\nwrong command\n\n

# Разбор команды для дальнейшего выполнения. Возвращает список команд для выполнения
# metrics_dict = {
#   'palm.cpu': [(1150864247, 0.5), (1150864248, 0.5)],
#   'eardrum.cpu': [(1150864250, 3.0), (1150864251, 4.0)],
#   'eardrum.memory': [(1503320872, 4200000.0)]
# }   put palm.cpu 23.7 1150864247\n
# get *\n  get palm.cpu\n  ok\npalm.cpu 2.0 1150864247\npalm.cpu 0.5 1150864248\neardrum.cpu 3.0 1150864250\n\n
# data = 'put paaslm.cpu 23.7 1150864247\n'
# metrics_dict = {'palm.cpu': {1150864263: 23.7, 1150864259: 55.7}, 'pal.cpu': {1150864263: 83.7, 1150864200: 55.7}}
#
#
# def process_data(data):
#     result = 'ok\n'
#     messages = data.split("\n")
#     print(messages)
#     for command in messages:
#         if not command:
#             continue
#         try:
#             method, metric = command.strip().split(" ", 1)
#             print(ascii(method))
#             if method == "put":
#                 name, value, timestamp = metric.split()
#                 if name not in metrics_dict:
#                     metrics_dict[name] = {}
#                 metrics_dict[name][int(timestamp)] = float(value)
#                 return result + '\n'
#             elif method == "get":
#                 responses, result_dict, name = [], {}, metric
#                 if len(name.strip().split(" ")) != 1:
#                     raise ValueError("wrong command")
#                 if name != "*":
#                     result_dict = {name: metrics_dict.get(name, {})}
#                 if name == "*":
#                     result_dict = metrics_dict
#                 for name in result_dict.keys():
#                     for timestamp in sorted(result_dict[name]):
#                         responses.append(
#                             f"{name} {result_dict[name][timestamp]}"
#                             f" {timestamp}"
#                         )
#                 if responses:
#                     result += '\n'.join(responses) + '\n'
#                     return result + '\n'
#             else:
#                 raise ValueError("unknown method")
#         except ValueError:
#             raise ValueError("wrong command")
#     raise ValueError("wrong command")
#
# print(ascii(process_data(data)))
# print(metrics_dict)
#

import asyncio


class ClientError(Exception):
    pass


class EchoServerClientProtocol(asyncio.Protocol):
    metrics_dict = {}

    def __init__(self):
        super().__init__()
        self.transport = None
        self._buffer = b''

    def process_data(self, data):
        result = 'ok\n'
        messages = data.split("\n")
        for command in messages:
            if not command:
                continue
            try:
                method, metric = command.strip().split(" ", 1)
                if method == "put":
                    name, value, timestamp = metric.split()
                    if name not in self.metrics_dict:
                        self.metrics_dict[name] = {}
                    self.metrics_dict[name][int(timestamp)] = float(value)
                    return result + '\n'
                elif method == "get":
                    responses, result_dict, name = [], {}, metric
                    if len(name.strip().split(" ")) != 1:
                        raise ValueError("wrong command")
                    if name != "*":
                        result_dict = {name: self.metrics_dict.get(name, {})}
                    if name == "*":
                        result_dict = self.metrics_dict
                    for name in result_dict.keys():
                        for timestamp in sorted(result_dict[name]):
                            responses.append(
                                f"{name} {result_dict[name][timestamp]}"
                                f" {timestamp}"
                            )
                    if responses:
                        result += '\n'.join(responses) + '\n'
                    return result + '\n'
                else:
                    raise ValueError("unknown method")
            except ValueError:
                raise ClientError("wrong command")
        raise ClientError("wrong command")

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data: bytes):
        self._buffer += data
        decoded_data = self._buffer.decode('ISO-8859-1')
        if not decoded_data.endswith('\n'):
            return
        self._buffer = b''
        try:
            resp = self.process_data(decoded_data)
        except ClientError as err:
            self.transport.write(f"error\n{err}\n\n".encode())
            return
        self.transport.write(resp.encode())


def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        EchoServerClientProtocol,
        host, port
    )
    server = loop.run_until_complete(coro)
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == "__main__":
    run_server('127.0.0.1', 8888)
