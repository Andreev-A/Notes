"""
Вам дан объект класса SomeObject, содержащего три поля: integer_field, float_field и string_field:
class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""
Необходимо реализовать поведение:
- EventGet(<type>) создаёт событие получения данных соответствующего типа
- EventSet(<value>) создаёт событие изменения поля типа type(<value>)
Необходимо реализовать классы NullHandler, IntHandler, FloatHandler, StrHandler так, чтобы можно было создать цепочку:
chain = IntHandler(FloatHandler(StrHandler(NullHandler)))
Описание работы цепочки:
- chain.handle(obj, EventGet(int)) — вернуть значение obj.integer_field
- chain.handle(obj, EventGet(str)) — вернуть значение obj.string_field
- chain.handle(obj, EventGet(float)) — вернуть значение obj.float_field
- chain.handle(obj, EventSet(1)) — установить значение obj.integer_field =1
- chain.handle(obj, EventSet(1.1)) — установить значение obj.float_field = 1.1
- chain.handle(obj, EventSet("str")) — установить значение obj.string_field = "str"
"""

class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ""


class EventGet:
    def __init__(self, prop):
        self.kind = prop
        self.prop = None


class EventSet:
    def __init__(self, prop):
        self.kind = type(prop)
        self.prop = prop


class NullHandler:
    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, char, event):
        if self.__successor is not None:
            return self.__successor.handle(char, event)


class IntHandler(NullHandler):
    def handle(self, char, event):
        if event.kind == int:
            if event.prop is None:
                return char.integer_field
            else:
                char.integer_field = event.prop
        else:
            return super().handle(char, event)


class FloatHandler(NullHandler):
    def handle(self, char, event):
        if event.kind == float:
            if event.prop is None:
                return char.float_field
            else:
                char.float_field = event.prop

        else:
            return super().handle(char, event)


class StrHandler(NullHandler):
    def handle(self, char, event):
        if event.kind == str:
            if event.prop is None:
                return char.string_field
            else:
                char.string_field = event.prop
        else:
            return super().handle(char, event)

#
# obj = SomeObject()
# obj.integer_field = 42
# obj.float_field = 3.14
# obj.string_field = "some text"
# chain = IntHandler(FloatHandler(StrHandler(NullHandler)))
# print(chain.handle(obj, EventGet(int)))
# print(chain.handle(obj, EventGet(float)))
# print(chain.handle(obj, EventGet(str)))
# chain.handle(obj, EventSet(100))
# print(chain.handle(obj, EventGet(int)))
# chain.handle(obj, EventSet(0.5))
# print(chain.handle(obj, EventGet(float)))
# chain.handle(obj, EventSet('new text'))
# print(chain.handle(obj, EventGet(str)))
#
######################################################################################################################
# решение от создателей курса
######################################################################################################################
# E_INT, E_FLOAT, E_STR = "INT", "FLOAT", "STR"
#
#
# class EventGet:
#     def __init__(self, prop):
#         self.kind = {int: E_INT, float: E_FLOAT, str: E_STR}[prop];
#         self.prop = None;
#
#
# class EventSet:
#     def __init__(self, prop):
#         self.kind = {int: E_INT, float: E_FLOAT, str: E_STR}[type(prop)];
#         self.prop = prop;
#
#
# class NullHandler:
#     def __init__(self, successor=None):
#         self.__successor = successor
#
#     def handle(self, obj, event):
#         if self.__successor is not None:
#             return self.__successor.handle(obj, event)
#
#
# class IntHandler(NullHandler):
#     def handle(self, obj, event):
#         if event.kind == E_INT:
#             if event.prop is None:
#                 return obj.integer_field
#             else:
#                 obj.integer_field = event.prop;
#         else:
#             return super().handle(obj, event)
#
#
# class StrHandler(NullHandler):
#     def handle(self, obj, event):
#         if event.kind == E_STR:
#             if event.prop is None:
#                 return obj.string_field
#             else:
#                 obj.string_field = event.prop;
#         else:
#             return super().handle(obj, event)
#
#
# class FloatHandler(NullHandler):
#     def handle(self, obj, event):
#         if event.kind == E_FLOAT:
#             if event.prop is None:
#                 return obj.float_field
#             else:
#                 obj.float_field = event.prop;
#         else:
#             return super().handle(obj, event)
