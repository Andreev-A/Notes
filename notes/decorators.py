# Декоратор это функция принимающая функцию и возвращающая другую функцию.
# Чаще всего используются чтобы модифицировать поведение каких-то input_file (может семейства input_file)
# Обычно input_file внутри декораторов называют - wrapped, decorated, inner

# def decorator(func):
#    return func  # простейший декоратор принимает функцию и возвращающет ее же

# @decorator  # пример записи и смысл -> decorated = decorator(decorated)
# def decorated():
#    print('Hello!')

# def decorator(func):  # простой декоратор принимает input_file
#    def new_func():  # определяет внутри новую input_file
#        pass
#    return new_func  # возвращает новую input_file
# @decorator
# def decorated():
#    print('Hello!')
# print(decorated())  # не вернется 'Hello!' так как вызовется new_func
# print(decorated.__name__)  # new_func

# import functools
# def logger(func):  # Написать декоратор, который записывает в лог результат декорируемой функции
#     # def wrapped(num_list):  # первый вариант, принимает только num_list
#     #     result_dict = func(num_list)
#     #     with open('log.txt', 'w') as input_file:
#     #         input_file.write(str(result_dict))
#     #     return result_dict
#     # return wrapped  #########################################################################################
#     @functools.wraps(func)  # подменяет (для интроспекции или отладки) в doc. string на название исходной input_file->summator
#     def wrapped(*args, **kwargs):  # второй вариант, принимает *args, **kwargs
#         result_dict = func(*args, **kwargs)
#         with open('log.txt', 'w') as input_file:
#             input_file.write(str(result_dict))
#         return result_dict
#     return wrapped  ############################################################################################
# @logger
# def summator(num_list):  # определен сумматор, он будет применяться с @logger
#     return sum(num_list)
# print('Summator: {}'.format(summator([1, 2, 3, 4, 5])))  # Summator: 15
# print(summator.__name__)  # summator или wrapped(без применения @functools.wraps(func))

# Написать декоратор с параметром, который записывает лог в указанный файл
# def logger(filename):  # вызывается input_file logger, который принимает не input_file, а имя файла, но возвращает decorator(summator)
#     def decorator(func):  # декоратор принимает input_file (summator) и возвращает новую input_file wrapped, кот. подменяет summator
#         def wrapped(*args, **kwargs):  # подменяет input_file summator
#             result_dict = func(*args, **kwargs)  # выполняется input_file summator
#             with open(filename, 'w') as input_file:
#                 input_file.write(str(result_dict))  # записывается результат ее выполнения в файл
#             return result_dict
#         return wrapped
#     return decorator  # вернется decorator, который будет применяться к input_file summator
# @logger('new_log.txt')  # применяется декоратор к input_file summator с параметром имя файла, куда писать лог
# def summator(num_list):
#     return sum(num_list)
# # summator = logger('log.txt')(summator) - так примерно работает
# summator([1, 2, 3, 4, 5, 6, 7])
# with open('new_log.txt', 'r') as input_file:
#     print(input_file.read())

# # Работа с двумя декораторами - цепочка "ченить"
# def first_decorator(func):  # просто принтят и вызывают input_file (для примера)
#     def wrapped():
#         print('Inside first_decorator product')
#         return func()
#     return wrapped
# def second_decorator(func):  # просто принтят и вызывают input_file (для примера)
#     def wrapped():
#         print('Inside second_decorator product')
#         return func()
#     return wrapped
# @first_decorator  # например залогинен ли пользователь
# @second_decorator  # например переданы данные
# def decorated():
#     print('Finally called...')
# # decorated = first_decorator(second_decorator(decorated)) - сначала second_decorator(decorated) -> вернули wrapped,
# # потом first_decorator(wrapped) -> вернули wrapped (из first_decorator) и она становится decorated() - далее печать 1
# # и вернули wrapped (из second_decorator) - далее печать 2 и вернули decorated
# decorated()
# # вывод:
# # Inside first_decorator product
# # Inside second_decorator product
# # Finally called...

# def bold(func):
#     def wrapped():
#         return "<b>" + func() + "</b>"
#     return wrapped
# def italic(func):
#     def wrapped():
#         return "<i>" + func() + "</i>"
#     return wrapped
# @bold
# @italic
# def hello():
#     return "hello world"
# # hello = bold(italic(hello)) - так примерно работает
# print(hello())  # <b><i>hello world</i></b> - внутри b(bold) вызывается i(italic), а потом (hello)

# # Чтобы передавать данные между функциями, модулями или разными системами используются форматы данных. Одним из самых
# # популярных форматов является JSON. Напишите декоратор to_json, который можно применить к различным функциям, чтобы
# # преобразовывать их возвращаемое значение в JSON-формат. Не забудьте про сохранение корректного имени декорируемой
# # функции.
# import functools
# import json
#
#
# def to_json(func):
#
#     @functools.wraps(func)
#     def wrapped(*args, **kwargs):
#         result_dict = func(*args, **kwargs)
#         return json.dumps(result_dict)
#
#     return wrapped
# # Несмотря на простоту задачи, похожий декоратор так или иначе встречается в каждом современном веб-приложении на
# # Python. Задание помогло нам разобраться с тем, как работают обычные декораторы, и обратить внимание на несколько
# # моментов. Во-первых, использование декоратора wraps поможет вам избежать проблем с отладкой и логированием,
# во-вторых, декораторы практически всегда пишутся так, чтобы их можно было применить к любой функции, то есть в
# определении новой функции используются *args и **kwargs.


######################################################################################################################
from abc import ABC, abstractmethod


class Delivery():
    """
    Класс описывающий объект, содержащий информацию о доставке для заказа
    """

    # для упрощения кода, пусть будет только один атрибут
    # time_delivery - время доставки, не будем добавлять id
    # заказа и другие "нужные" данные
    def __init__(self, time_delivery=None):
        self.time_delivery = time_delivery or 10

    def get_time_delivery(self):
        """возвращает время доставки по заказу"""
        return self.time_delivery


# На время доставки могут влиять разные факторы - проведение
# специальных акций, выбор специальных условий при заказе,
# например: экспресс доставка или оплата наличными. В начальный
# момент времени (при написании кода) нельзя учесть все возможные
#  действия, которые возможно будут добавлены.
class AbstractDeliveryAction(ABC, Delivery):
    """Абстрактный для всех действий класс"""

    def __init__(self, base):
        self.base = base
        self.actions = []

    @abstractmethod
    def get_time_delivery(self):
        pass


class SpecialOffer(AbstractDeliveryAction):
    """Специальное предложение - сокращает срок доставки на 3 дня"""

    def get_time_delivery(self):
        return self.base.get_time_delivery() - 3


class ExpressDelivery(AbstractDeliveryAction):
    """Экспресс доставка сокращает срок доставки на 10 дней"""

    def get_time_delivery(self):
        return self.base.get_time_delivery() - 5


class CardPayment(AbstractDeliveryAction):
    """Оплата картой увеличивает срок доставки на 1 день"""

    def get_time_delivery(self):
        return self.base.get_time_delivery() + 1


# обратите внимание, что мы не изменяем непосредственно self.base
# а возвращаем его изменененную копию, так происходит магия декораторов
# создадим заказ
order = Delivery()
print(order.get_time_delivery())
# будем применять действия к заказу, в зависимости от желания
# заказчика и действующих акций
order_expr = ExpressDelivery(order)
print(order_expr.get_time_delivery())
order_expr_spec = SpecialOffer(order_expr)
print(order_expr_spec.get_time_delivery())
order_total = CardPayment(order_expr_spec)
print(order_total.get_time_delivery())

# уберем экспресс доставку, если вдруг заказчик передумал
order_expr_spec.base = order_expr_spec.base.base
print(order_total.get_time_delivery())
# вывод справа в окне терминала -->
# такая реализация позволяет без проблем добавлять новые действия
# и их можно без проблем применять к уже существующим заказам

# Это учебный пример, поэтому простой и немного натянут за уши :)







