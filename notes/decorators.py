# Декоратор это функция принимающая функцию и возвращающая другую функцию.
# Чаще всего используются чтобы модифицировать поведение каких-то f (может семейства f)
# Обычно f внутри декораторов называют - wrapped, decorated, inner

# def decorator(func):
#    return func  # простейший декоратор принимает функцию и возвращающет ее же

# @decorator  # пример записи и смысл -> decorated = decorator(decorated)
# def decorated():
#    print('Hello!')

# def decorator(func):  # простой декоратор принимает f
#    def new_func():  # определяет внутри новую f
#        pass
#    return new_func  # возвращает новую f
# @decorator
# def decorated():
#    print('Hello!')
# print(decorated())  # не вернется 'Hello!' так как вызовется new_func
# print(decorated.__name__)  # new_func

# import functools
# def logger(func):  # Написать декоратор, который записывает в лог результат декорируемой функции
#     # def wrapped(num_list):  # первый вариант, принимает только num_list
#     #     result_dict = func(num_list)
#     #     with open('log.txt', 'w') as f:
#     #         f.write(str(result_dict))
#     #     return result_dict
#     # return wrapped  #########################################################################################
#     @functools.wraps(func)  # подменяет (для интроспекции или отладки) в doc. string на название исходной f->summator
#     def wrapped(*args, **kwargs):  # второй вариант, принимает *args, **kwargs
#         result_dict = func(*args, **kwargs)
#         with open('log.txt', 'w') as f:
#             f.write(str(result_dict))
#         return result_dict
#     return wrapped  ############################################################################################
# @logger
# def summator(num_list):  # определен сумматор, он будет применяться с @logger
#     return sum(num_list)
# print('Summator: {}'.format(summator([1, 2, 3, 4, 5])))  # Summator: 15
# print(summator.__name__)  # summator или wrapped(без применения @functools.wraps(func))

# Написать декоратор с параметром, который записывает лог в указанный файл
# def logger(filename):  # вызывается f logger, который принимает не f, а имя файла, но возвращает decorator(summator)
#     def decorator(func):  # декоратор принимает f (summator) и возвращает новую f wrapped, кот. подменяет summator
#         def wrapped(*args, **kwargs):  # подменяет f summator
#             result_dict = func(*args, **kwargs)  # выполняется f summator
#             with open(filename, 'w') as f:
#                 f.write(str(result_dict))  # записывается результат ее выполнения в файл
#             return result_dict
#         return wrapped
#     return decorator  # вернется decorator, который будет применяться к f summator
# @logger('new_log.txt')  # применяется декоратор к f summator с параметром имя файла, куда писать лог
# def summator(num_list):
#     return sum(num_list)
# # summator = logger('log.txt')(summator) - так примерно работает
# summator([1, 2, 3, 4, 5, 6, 7])
# with open('new_log.txt', 'r') as f:
#     print(f.read())

# # Работа с двумя декораторами - цепочка "ченить"
# def first_decorator(func):  # просто принтят и вызывают f (для примера)
#     def wrapped():
#         print('Inside first_decorator product')
#         return func()
#     return wrapped
# def second_decorator(func):  # просто принтят и вызывают f (для примера)
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





