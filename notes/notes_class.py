# type(obj)  # узнать тип класса
# print(isinstance(13, float))  # принадлежит ли классу
# obj.__dict__  # сюда записываются атрибуты объекта
# __init__  # вызывается при создании экземпляра
# __str__ # позволяет переопределить как будет печататься объект
# __repr__  # переопределить как внутренное представление объекта будет выводится (в списке)
#  __dict__  # словарь - хранит атрибуты экземпляра класса или  mappingproxy (похож на словарь) самого класса
# __doc__  # описание как из класса, так и из экземпляра
# __class__  # у экземпляра можем получить класс к  которому принадлежит
# dir() - методы у объекта
# Экземпляры класса хешируются, то есть могут быть ключами словаря

# # Конструктор экземпляра класса
# class Planet:
#     def __new__(cls, *args, **kwargs):
#         print("__new__ called")
#         obj = super().__new__(cls)  # создание нового экземпляра класса (super возвращает родителя нашего класса- obj)
#         return obj
#     def __init__(self, name):
#         print("__init__ called")
#         self.name = name
# earth = Planet("Earth")
# __new__ called
# __init__ called
# То есть при вызове Planet("Earth") произошло примерно следующее:
# planet = Planet.__new__(Planet, "Earth")
# if isinstance(planet, Planet):
#     Planet.__init__(planet, "Earth")

# # Работа с методами экземпляра
# class Human:
#     def __init__(self, name, age=0):
#         self.name = name
#         self.age = age
# class Planet:
#     def __init__(self, name, population=None):
#         self.name = name
#         self.population = population or []
#     def add_human(self, human):  # метод экземпляра класса (принимает экземпляр класса Human)
#         print(input_file"Welcome to {self.name}, {human.name}!")
#         self.population.append(human)
# mars = Planet("Mars")  # создали планету
# bob = Human("Bob")  # создали человека
# mars.add_human(bob)  # добавили на планету человека
# # Welcome to Mars, Bob!
# print(mars.population)  # [<__main__.Human object at 0x10e416780>] - добавился человек

# # Вызов методов из методов
# class Human:
#     def __init__(self, name, age=0):
#         self._name = name  # соглашение _name пользоваться не рекомендуется (может не быть этих атрибутов или методов)
#         self._age = age  # соглашение _name пользоваться не рекомендуется (может не быть этих атрибутов или методов)
#
#     def _say(self, text):  # соглашение _name пользоваться не рекомендуется (может не быть этих атрибутов или методов)
#         print(text)
#
#     def say_name(self):  # публичный метод - можно пользоваться
#         self._say(input_file"Hello, I am {self._name}")
#
#     def say_how_old(self):  # публичный метод - можно пользоваться
#         self._say(input_file"I am {self._age} years old")
# bob = Human("Bob", age=29)
# bob.say_name()
# bob.say_how_old()
# # Hello, I am Bob
# # I am 29 years old
# print(bob._name)  # не рекомендуется! может не быть в другом обновлении
# bob._say("Whatever we want")  # не рекомендуется! может не быть в другом обновлении
# # Bob
# # Whatever we want

# Метод класса - @classmethod - не привязан к конкретному экземпляру, вовлекает сам класс (оперирует классом)
# К этому методу можно обращаться от экземпляра класса
# Метод первым аргументом принимает класс
# К этому методу можно обращаться от имени класса
# class Event:
#     def __init__(self, description, event_date):
#         self.description = description
#         self.date = event_date
#     def __str__(self):
#         return input_file"Event \"{self.description}\" at {self.date}"
# from datetime import date
# event_description = "Рассказать, что такое @classmethod"
# event_date = date.today()
# event = Event(event_description, event_date)
# print(event)  # Event "Рассказать, что такое @classmethod" at 2017 - 07 - 09
#
# def extract_description(user_string):  # ввод например в мессенджере (добавить событие в календарь пользователя)
#     return "открытие чемпионата мира по футболу"
# def extract_date(user_string):  # ввод например в мессенджере (добавить событие в календарь пользователя)
#     return date(2018, 6, 14)
# class Event:  # обработка на серверной стороне
#     def __init__(self, description, event_date):
#         self.description = description
#         self.date = event_date
#     def __str__(self):
#         return input_file"Event \"{self.description}\" at {self.date}"
#     @classmethod  # встроенный объект, не надо импортировать - делает метод методом класса (в методе аргумент cls)
#     def from_string(cls, user_input):
#         description = extract_description(user_input)
#         date = extract_date(user_input)
#         return cls(description, date)
# event = Event.from_string("добавить в мой календарь открытие чемпионата мира по футболу на 14 июня 2018 года")
# print(event)  # Event "открытие чемпионата мира по футболу" at 2018 - 06 - 14

# Статический метод класса - @ staticmethod - нет ссылки на экземпляр или класс (input_file с обращением от класса, экземпляра)
# Метод не принимает дополнительных аргументов кроме указанных программистом (просто input_file)
# К этому методу можно обращаться от экземпляра класса
# К этому методу можно обращаться от имени класса
# class Human:
#     def __init__(self, name, age=0):
#         self.name = name
#         self.age = age
#     @staticmethod  # встроенный объект, не надо импортировать (принимает аргументы которые ему передают)
#     def is_age_valid(age):  # нет ни self ни cls
#         return 0 < age < 150
# # можно обращаться от имени класса
# Human.is_age_valid(35)  # True
# # или от экземпляра:
# human = Human("Old Bobby")
# human.is_age_valid(234)  # False

# Вычисляемые свойства класса (property)
# Property позволяют изменять поведение и выполнять какую-то вычислительную работу при обращении к атрибуту экземпляра,
# либо при изменении атрибута, либо при его удалении.
# class Robot:
#     def __init__(self, power):
#         self.power = power
# wall_e = Robot(100)
# wall_e.power = 200
# print(wall_e.power)  # 200
# wall_e.power = -20  # неправильно ставить отрицательную мощность - в этом случае хотелось бы 0
# class Robot:  # так бы написали рефакторинг, можно пользоваться - но кто использует класс должен поменять свой код
#     def __init__(self, power):
#         self.power = power
#     def set_power(self, power):  # можно сделать так, но если уже работает - надо менять код на стороне пользователя
#         if power < 0:
#             self.power = 0
#         else:
#             self.power = power
# wall_e = Robot(100)
# wall_e.set_power(-20)
# print(wall_e.power)  # 0
# class Robot:
#     def __init__(self, power):
#         self._power = power  # _power приватный атрибут
#     power = property()  # встроенный объект не надо импортировать
#     @power.setter  # выполняем когда надо менять атрибут
#     def power(self, value):
#         if value < 0:
#             self._power = 0  # возвращаем приватное значение атрибута
#         else:
#             self._power = value  # возвращаем приватное значение атрибута
#     @power.getter  # выполняем когда читаем атрибут
#     def power(self):
#         return self._power  # возвращаем приватное значение атрибута
#     @power.deleter  # выполняем при удаленни атрибута
#     def power(self):
#         print("make robot useless")
#         del self._power
# wall_e = Robot(100)
# wall_e.power = -20
# print(wall_e.power)  # 0
# del wall_e.power  # make robot useless
# class Robot:
#     def __init__(self, power):
#         self._power = power
#     @property  # когда надо модифицировать работу при чтении
#     def power(self):
#         # здесь могут быть любые полезные вычисления
#         return self._power
# wall_e = Robot(200)
# print(wall_e.power)  # 200

# Использование property в Python
# Функция property — создает вычисляемое свойство, которое позволяет использовать методы класса в качестве свойств
# объектов. Свойство — это аттрибут класса, который может считывать или записывать информацию. Использование property
# создает дескриптор, который позволяет создавать свойства объекту.
# Проблема
# Давайте рассмотрим пример. Существует класс человек, возраст которого не может быть меньше 0 и больше 120. Типичная
# ООП программа будет выглядеть примерно так:
# class Human:
#     """Человек, возраст которого не может быть больше 120 и меньше 0"""
#
#     def __init__(self, age=0):
#         self.set_age(age)
#
#     def get_age(self):
#         return self.age
#
#     def set_age(self, age):
#         if 0 <= age < 120:
#             self.age = age
#         else:
#             self.age = 0
# Как мы видим в этой реализации присутствуют некоторые проблемы и давайте их рассмотрим внимательно.
# Создадим экземпляр 30 летнего человека, и проверим корректность введенных данных.
# h = Human(age=30)
# print(h.get_age())  # 30
# Число 30 входит в рамки человеческой жизни и проблем у нас не возникло.
# Попробуем ввести возраст вне рамок человеческой жизни
# h = Human(age=150)
# print(h.get_age())  # 0
# В данном примере мы обратились к методу класса, который проверил входные данные, из-за чего нам не удалось выставить
# некорректный возраст.
# Но мы можем напрямую обратиться к аттрибуту self.age и указать абсолютно любой возраст.
# h.age = 150
# print(h.age)  # 150
# Таким способом мы нарушаем алгоритм работы нашего класса, что является серьезной проблемой.
# Решение
# Для решения этой проблемы существуют два способа. Первый способ подразумевает использование декоратора функции, а
# второй способ указывает в функции property getter, setter и deleter.
# Использование декоратора
# @property — это декоратор, который обрабатывает получение, установку и удаление переменных класса так, как это было
# задумано в Python. Код для вышеописанного сценария будет выглядеть теперь так:
# class Human:
#     """Человек, возраст которого не может быть больше 120 и меньше 0"""
#
#     def __init__(self, age=0):
#         self.__age = age
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if 0 <= age < 120:
#             self.__age = age
#         else:
#             self.__age = 0
# Наш код стал более лаконичным, но давайте разберемся по пунктам что же все таки изменилось и на что это повлияло.
# Мы использовали декоратор @property, который создает для декорируемой функции геттер.
# Затем мы использовали декоратор @age.setter, который создает для декорируемой функции сеттер. Сеттер определяет, что
# делать при установке значения переменной.
# Обратите внимание, что обе функции имеют одинаковое имя. Это необходимо для работы программы.
# Попробуем установить некорректное значение и посмотрим что получится:
# h = Human(age=30)
# h.age = 150
# print(h.age)  # 0
# Используя декоратор @property мы ограничиваем возможность указания значений переменным в классе.
# Прямое указание функций
# Во втором варианте использование property мы описываем функцию для установки значения и получения значения.
# class Human:
#     """Человек, возраст которого не может быть больше 120 и меньше 0"""
#
#     def __init__(self, age=0):
#         self.set_age(age)
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, age):
#         if 0 <= age < 120:
#             self.__age = age
#         else:
#             self.__age = 0
#
#     age = property(get_age, set_age)
# # Как видите, нам просто нужно было изменить переменные и добавить специальную строку age = property(get_age, set_age),
# # которая залатала дыры в нашем исходном коде и сэкономила нам кучу времени!
# # Произведем проверку
# h = Human(age=30)
# h.age = 150
# print(h.age)  # 0
# Я не упомянул в статье о так называемых deleter.

# Для чего же нужно наследование классов? Прежде всего оно нужно для изменения поведения конкретного класса, а также
# расширения его функционала.
# class Pet:
#     def __init__(self, name=None):
#         self.name = name
# class Dog(Pet):  # наследуется от класса Pet (базовый, супер) наследуются все атрибуты и методы
#     def __init__(self, name, breed=None):
#         super().__init__(name)  # вызываем метод init из родительского класса с помощью super
#         self.breed = breed
#     def say(self):  # добавляем собственный метод
#         return '{0}: waw'.format(self.name)
# dog = Dog('Шарик', 'Дворняга')
# print(dog.name)  # Шарик
# print(dog.say())  # Шарик: waw
# # Множественное наследование - не стоит создавать большое количество классов примесей
# import json
# class ExportJSON:  # класс примесь
#     def to_json(self):
#         return json.dumps({
#             'name': self.name,
#             'breed': self.breed
#         })
# class ExDog(Dog, ExportJSON):
#     pass
# dog = ExDog('Шарик', 'Дворняга')
# print(dog.to_json())
# {"name": "\u0428\u0430\u0440\u0438\u043a", "breed": "\u0414\u0432\u043e\u0440\u043d\u044f\u0433\u0430"}
# В Python есть две встроенные функции, которые работают с наследованием:
# Используется isinstance() для проверки является ли объект экземпляром нужного нам класса: будет только в том случае,
# если есть или какой-то класс, производный от isinstance(obj, int)True obj.__class__int int
# Используется issubclass() для проверки наследования класса: is, поскольку является подклассом . Тем не менее, это так
# не подкласс issubclass(bool, int)Trueboolintissubclass(float, int)Falsefloatint
# Используется issubclass()для проверки наследования класса - любой класс является потомком object

# Поиск атрибутов и методов объекта, линеаризация класса
#    object
#    /    \
#   /      \
#  Pet     ExportJSON
#   |      /
#  Dog    /
#    \   /
#    ExDog
# Method Resolution Order
# print(ExDog.__mro__)  # (<class '__main__.ExDog'>, <class '__main__.Dog'>, <class '__main__.Pet'>,
                        # <class '__main__.ExportJSON'>, <class 'object'>)
# Использование super()
# class ExDog(Dog, ExportJSON):
#     def __init__(self, name, breed=None):
#         # вызов метод по MRO
#         super().__init__(name, breed)  # super без параметров - равносильно указали сам класс и передали
#         # туда объект self -> super(ExDog, self).__init__(name)
# class WoolenDog(Dog, ExportJSON):
#     def __init__(self, name, breed=None):
#         # явное указание метода конкретного класса (в super надо передать родителя этого класса Dog для обращения к Pet)
#         super(Dog, self).__init__(name)
#         self.breed = 'Шерстяная собачка породы {0}'.format(breed)
# dog = WoolenDog("Жучка", breed="Такса")
# print(dog.breed)  # Шерстяная собачка породы Такса

# # Разрешение конфликта имен, name mangling
# class Pet:
#     def __init__(self, name=None):
#         self.name = name
# class Dog(Pet):
#     def __init__(self, name, breed=None):
#         super().__init__(name)
#         self.__breed = breed  # приватный атрибут
#     def say(self):
#         return "{0}: waw!".format(self.name)
#
#     def get_breed(self):
#         return self.__breed  # можно обращаться только в классе
# class ExportJSON:
#     def to_json(self):
#         pass
# class ExDog(Dog, ExportJSON):
#     def get_breed(self):
#         return "порода: {0} - {1}".format(self.name, self.__breed)  # поменять, чтобы увидеть атрибут на -> _Dog__breed
# dog = ExDog("Фокс", "Мопс")
# # dog.get_breed()  # ошибка, не видим приватный атрибут __breed
# print(dog.__dict__)  # {'name': 'Фокс', '_Dog__breed': 'Мопс'}

# Композиция классов или наследование?
# class Pet:
#     pass
# class Dog(Pet):
#     pass
# class ExportJSON(Pet):
#     pass
# class ExDog(Dog, ExportJSON):
#     pass
# # Композиция VS наследование
# class ExportJSON:
#     def to_json(self):
#         pass
# class ExportXML:
#     def to_xml(self):
#         pass
# class ExDog(Dog, ExportJSON, ExportXML):
#     pass
#
# dog = ExDog("Фокс", "мопс")
# dog.to_xml()
# dog.to_json()
### Композиция классов против наследования, пример буду вводить в онлайн
import json
class Pet:
    pass
    # def __init__(self, name):
    #     self.name = name
class Dog(Pet):
    pass
    # def __init__(self, name, breed=None):
    #     super().__init__(name)
    #     self.breed = breed
    # def say(self):
    #     return "{0}: waw".format(self.name)
# class PetExport:  # предназначен только для наследования
#     def export(self, dog):
#         raise NotImplementedError
# class ExportXML(PetExport):
#     def export(self, dog):
#         return """<xml version="1.0" encoding="utf-8">
# <dog>
#   <name>{0}</name>
#   <breed>{1}</breed>
# </dog>
# """.format(dog.name, dog.breed)
# class ExportJSON(PetExport):
#     def export(self, dog):
#         return json.dumps({
#             "name": dog.name,
#             "breed": dog.breed,
#         })
# class ExDog(Dog):  # не будем применять множественное наследование, будем расширять класс ExDog
#     def __init__(self, name, breed=None, exporter=None):
#         super().__init__(name, breed)  # вызов конструктора базового класса
#         self._exporter = exporter or ExportJSON()  # дополнительный объект для экспорта данных
#         if not isinstance(self._exporter, PetExport):  # проверка
#             raise ValueError("bad export instance value", exporter)
#
#     def export(self):  # метод экспорт
#         return self._exporter.export(self)
#
# fox = ExDog("Фокс", "мопс", exporter=ExportXML())
# print(fox.export())
# <xml version="1.0" encoding="utf-8">
# <dog>
#   <name>Фокс</name>
#   <breed>мопс</breed>
# </dog>
# muhtar = ExDog("Мухтар", "питбуль")
# print(muhtar.export())
# {"name": "\u041c\u0443\u0445\u0442\u0430\u0440", "breed": "\u043f\u0438\u0442\u0431\u0443\u043b\u044c"}
print(isinstance(Pet(), object))
print(isinstance(Dog, Dog))
print(isinstance(Pet(), Dog))
print(isinstance(Dog(), Dog))
print(isinstance(Dog(), Pet))

# Функция isinstance() в Python, принадлежность экземпляра к классу.
# Синтаксис:
# isinstance(object, classinfo)
# Параметры:
# object - объект, требующий проверки,
# classinfo - класс, кортеж с классами или рекурсивный кортеж кортежей или с версии Python 3.10 может быть объединением нескольких типов (например int | str).
# Возвращаемое значение:
# bool.
# Позволяет проверить принадлежность экземпляра к классу.
# Синтаксис:
# isinstance(object, classinfo)
# Параметры:
# object - объект, требующий проверки,
# classinfo - класс, кортеж с классами или рекурсивный кортеж кортежей или с версии Python 3.10 может быть объединением нескольких типов (например int | str).
# Возвращаемое значение:
# bool.
# Описание:
# Функция isinstance() вернет True, если проверяемый объект object является экземпляром указанного класса (классов) или его подкласса (прямого, косвенного или виртуального).
#
# Если объект object не является экземпляром данного типа, то функция всегда возвращает False.
#
# Функцией isinstance() можно проверить класс, кортеж с классами, либо рекурсивный кортеж кортежей. Другие типы последовательностей аргументом classinfo не поддерживаются.
#
# Если аргумент classinfo не является классом, либо кортежем с классами, а с версии Python 3.10 записью, объединяющей нескольких типов (например int | str), то возбуждается исключение TypeError.
#
# Изменено в версии 3.10: аргумент classinfo может иметь тип Union и записываться как побитовое или - |.
#
# >>> isinstance(1, int | str)
# # True
# >>> isinstance("", int | str)
# # True
# Доступ к пользовательскому типу для объекта union можно получить из types.UnionType и использовать для проверок isinstance(). Невозможно создать экземпляр объекта из типа:
#
# >>> import types
# >>> isinstance(int | str, types.UnionType)
# # True
# >>> types.UnionType()
# # Traceback (most recent call last):
# #   file "<stdin>", line 1, in <module>
# # TypeError: cannot create 'types.UnionType' instances
# Примеры проверок принадлежности экземпляра к классу.
# Взгляните на следующий код:
#
# >>> a = 3
# >>> isinstance(a, object)
# # True
# >>> type(a) == object
# # False
# >>> issubclass(type(a), object)
# # True
# Молодые программисты часто не понимают что здесь происходит. Давайте разбираться...
#
# Функция type() с одним аргументом object возвращает тип объекта - точный класс, из которого был создан переданный аргумент object. Мы знаем, что все целые числа в Python являются типом int. Это означает, что проверка объекта type(3) == object в точности эквивалентна проверке объекта int == object, что однозначно неверно.
#
# В Python, как это известно - все является объектом, следовательно дочерний класс (в данном случае int) наследуется от родительского (в данном случае object) и считается, что такое поведение имеет отношение is a. Отношение is a - это то, что проверяет функция isinstance().
#
# Существует аналогичная функция issubclass() для проверки того же отношения, только для класса вместо экземпляра этого класса. В большинстве случаев isinstance(x, y) == issubclass(type(x), y).
#
# Классы всегда имеют одну и ту же ссылку в ​​одной сессии интерпретатора, поэтому можно использовать оператор is вместо оператора == для сравнения. Таким образом, type(3) is int будет истинным.
#
# Изобразим сказанное выше на примере:
#
# class Base:
#     def __init__(self):
#         self.foo='foo'
#
# class Sub(Base):
#     def __init__(self):
#         super().__init__()
#
# >>> obj = Base()
# >>> sub_obj = Sub()
# >>> isinstance(obj, Base)
# # True
# >>> isinstance(obj, Sub)
# # False
# >>> isinstance(sub_obj, Base)
# # True
# >>> isinstance(sub_obj, Sub)
# # True
# >>> type(sub_obj) == Base
# # False
# >>> type(sub_obj)
# # <class '__main__.Sub'>
# >>> type(sub_obj) == Sub
# # True
# >>> issubclass(type(sub_obj), Base)
# # True
# Общие приемы проверок.
# >>> x = 1
# >>> isinstance(x, int)
# # True
# >>> x = [1, 2, 3]
# >>> isinstance(x, list)
# # True
# >>> x = (1, 2, 3)
# >>> isinstance(x, tuple)
# # True
#
# # Проверим, является ли строка 'Hello' одним из типов, описанных в параметре type
# >>> isinstance('Hello', (float, int, str, list, dict, tuple))
# # True
#
# # Проверка, на принадлежность к экземпляром myObj
# class myObj:
#   name = "John"
#
# y = myObj()
# >>> isinstance(y, myObj)
# # True