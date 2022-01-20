# """Код программы рисования пейзажа"""
# import graphics as gr
#
#
# def main():
#     window = gr.GraphWin("My Image", 600, 600)
#     draw_image(window)
#     window.getMouse()
#
#
# def draw_image(window):
#     house_x, house_y = window.width // 2, window.height * 2 // 3
#     house_width = window.width // 3
#     house_height = house_width * 4 // 3
#
#     draw_background(window)
#     draw_house(window, house_x, house_y, house_width, house_height)
#
#
# def draw_background(window):
#     earth = gr.Rectangle(gr.Point(0, window.height // 2),
#                          gr.Point(window.width - 1, window.height - 1))
#     earth.setFill("green")
#     earth.draw(window)
#     scy = gr.Rectangle(gr.Point(0, 0),
#                        gr.Point(window.width - 1, window.height // 2))
#     scy.setFill("cyan")
#     scy.draw(window)
#
#
# def draw_house(window, x, y, width, height):
#     foundation_height = height // 8
#     walls_height = height // 2
#     walls_width = 7 * width // 8
#     roof_height = height - walls_height - foundation_height
#
#     draw_house_foundation(window, x, y, width, foundation_height)
#     draw_house_walls(window, x, y - foundation_height,
#                      walls_width, walls_height)
#     draw_house_roof(window, x, y - foundation_height - walls_height,
#                     width, roof_height)
#
#
# def draw_house_foundation(window, x, y, width, height):
#     foundation = gr.Rectangle(gr.Point(x - width // 2, y),
#                               gr.Point(x + width // 2, y - height))
#     foundation.setFill("brown")
#     foundation.draw(window)
#
#
# def draw_house_walls(window, x, y, width, height):
#     walls = gr.Rectangle(gr.Point(x - width // 2, y),
#                          gr.Point(x + width // 2, y - height))
#     walls.setFill("red")
#     walls.draw(window)
#     draw_house_window(window, x, y - height // 4,
#                       width // 3, height // 2)
#
#
# def draw_house_window(window, x, y, width, height):
#     glass = gr.Rectangle(gr.Point(x - width // 2, y),
#                          gr.Point(x + width // 2, y - height))
#     glass.setFill("blue")
#     line1 = gr.Line(gr.Point(x, y), gr.Point(x, y - height))
#     line2 = gr.Line(gr.Point(x - width // 2, y - height // 2),
#                     gr.Point(x + width // 2, y - height // 2))
#     glass.draw(window)
#     line1.draw(window)
#     line2.draw(window)
#     line1.setOutline("black")
#     line2.setOutline("black")
#     line1.setWidth(2)
#     line2.setWidth(2)
#
#
# def draw_house_roof(window, x, y, width, height):
#     roof = gr.Polygon(gr.Point(x - width // 2, y),
#                       gr.Point(x + width // 2, y),
#                       gr.Point(x, y - height))
#     roof.setFill("green")
#     roof.draw(window)
#
#
# if __name__ == "__main__":
#     main()

# Этот программный код нельзя назвать образцовым. Дело в том, что в функциях отсутствуют документ-строки, а
# документирование функций — это очень важно. Однако, в данном уроке нет цели обучить этому навыку. В ущерб
# перфекционизму мы здесь концентрируемся на парадигме структурного программирования, а особенно на навыке декомпозиции
# задачи и итеративном движении сверху-вниз.

#######################################################################################################################
# def main():
#     salary = calculate_salary()
#     print(salary)
#
#
# def calculate_salary():
#     """
#     Считает зарплату сотрудника ДПС, считывая исходные данные с клавиатуры.
#
#     :returns: зарплата сотрудника
#     """
#     sum_of_fines = 0
#     speed_of_auto, number_of_auto = read_data()
#     while not detect_chief(number_of_auto):
#         if speed_of_auto > 60:
#             sum_of_fines += calculate_fine(number_of_auto)
#         speed_of_auto, number_of_auto = read_data()
#     return sum_of_fines
#
#
# def read_data():
#     """
#     Считывает следущую строку данных.
#
#     :returns: tuple(int, str) - скорость, номер машины
#     """
#     data = input().split()
#     return data
#
#
# def detect_chief(number_of_auto):
#     """
#     Проверяет, принадлежит ли данный номер начальнику.
#
#     :param number_of_auto: номер автомобиля
#     :returns: True, если номер принадлежит начальнику, иначе False
#     """
#     return number_of_auto == "A999AA"
#
#
# def calculate_fine(number_of_auto):
#     """
#     Считает штраф для автомобиля с конкретным номером.
#
#     :param number_of_auto: номер автомобиля
#     :returns: Целое число, размер штрафа
#     """
#     if is_super_number(number_of_auto):
#         return 1000
#     elif is_good_number(number_of_auto):
#         return 500
#     else:
#         return 100
#
#
# def is_super_number(number_of_auto):
#     """
#     Проверяет, является ли номер «крутым» (совпадение трёх цифр)
#
#     :param number_of_auto: номер автомобиля
#     :returns: True, если номер «крутой», иначе False
#     """
#     return number_of_auto[1] == number_of_auto[2] == number_of_auto[3]
#
#
# def is_good_number(number_of_auto):
#     """
#     Проверяет, является ли номер «хорошим» (совпадение двух цифр)
#
#     :param number_of_auto: номер автомобиля
#     :returns: True, если номер «хороший», иначе False
#     """
#     return number_of_auto[1] == number_of_auto[2] or \
#            number_of_auto[1] == number_of_auto[3] or \
#            number_of_auto[2] == number_of_auto[3]
#
#
# if __name__ == "__main__":
#     main()

######################################################################################################################
# Паттерн Декоратор
# Паттерн декоратор относится к классу структурных паттернов проектирования. Его основная задача -- динамическое
# подключение дополнительной функциональности к объекту. При этом для подключения дополнительной функциональности
# используется не сложная иерархия подклассов, что является классическим решением данной задачи, а отдельная иерархия
# декораторов.
# Каждый из видов дополнительной функциональности, которая может быть добавлена к объекту, помещается в отдельный класс.
# Эти классы сами по себе небольшие, поэтому в них легко разобраться.
# В паттерн "Декоратор" входят оборачиваемый объект и сама иерархия декораторов. Каждый из декораторов реализует
# какое-то одно функциональное свойство. Это позволяет соблюдать один из SOLID принципов -- принцип единственной
# ответственности. Так мы можем подключить к классу только ту функциональность, которая необходима ему в данный момент.
# Для подключения нескольких функциональных свойств можно последовательно использовать несколько декораторов.
# Для создания паттерна "Декоратор" необходимы следующие классы:
# - Абстрактный объект (Component)
# - Оборачиваемый объект (на UML-диаграмме ConcreteComponent)
# - Абстрактный декоратор (Decorator)
# - Конкретный декоратор (ConcreteDecorator)
# Как видно из диаграммы, все декораторы по сути являются объектами, подобными самому компоненту. Из этого следует, что
# они реализуют одинаковый интерфейс. Согласно принципу подстановки Барбары Лисков у пользователя должна быть
# возможность корректного использования объекта-декоратора (то есть объекта, обернутого в декоратор), не зная об этом.
# Тут находится одно из слабых мест паттерна. Интерфейс объекта и интерфейс модифицированного объекта одинаковы. Это не
# всегда удобно, иногда для модифицированного объекта требуется отдельный интерфейс.
# Использование паттерна Декоратор
# При использовании паттерна декорируемый объект оборачивается в декоратор. Таким образом получается вложенная структура
# из декораторов. Отменить действие декоратора можно, если достать базовый объект из декоратора. Это можно сделать,
# обратившись к decorated_object.base. Аналогичным образом можно отменить эффект декоратора из середины иерархии. Для
# этого изменим базовый объект у внешнего декоратора на базовый объект декоратора, который необходимо удалить. Принцип
# похож на удаление элемента из середины односвязного списка.
# Пример использования Декоратора
# from abc import ABC, abstractmethod
#
#
# class Creature(ABC):
#     @abstractmethod
#     def feed(self):
#         pass
#
#     @abstractmethod
#     def move(self):
#         pass
#
#     @abstractmethod
#     def make_noise(self):
#         pass
#
#
# class Animal(Creature):
#     def feed(self):
#         print("I eat grass")
#
#     def move(self):
#         print("I walk forward")
#
#     def make_noise(self):
#         print("WOOO!")
#
#
# class AbstractDecorator(Creature):
#     def __init__(self, obj):
#         self.obj = obj  # в видеолекции вместо obj -> base
#
#     def feed(self):
#         self.obj.feed()
#
#     def move(self):
#         self.obj.move()
#
#     def make_noise(self):
#         self.obj.make_noise()
#
#
# class Swimming(AbstractDecorator):
#     def move(self):
#         print("I swim")
#
#     def make_noise(self):
#         print("...")
#
#
# class Flying(AbstractDecorator):
#     def move(self):
#         print("I fly")
#
#     def make_noise(self):
#         print("QUAAA!")
#
#
# class Predator(AbstractDecorator):
#     def feed(self):
#         print("I eat other animals")
#
#
# class Fast(AbstractDecorator):
#     def move(self):
#         self.obj.move()
#         print("Fast!")
#
#
# animal = Animal()  # наложение декораторов - создаем животное, добавляя созданные эффекты животных
# animal.feed()
# animal.move()
# animal.make_noise()
# print()
# animal = Swimming(animal)
# animal.feed()
# animal.move()
# animal.make_noise()
# print()
# animal = Predator(animal)
# animal.feed()
# animal.move()
# animal.make_noise()
# print()
# animal = Fast(animal)
# animal.feed()
# animal.move()
# animal.make_noise()
# print()
# animal = Fast(animal)
# animal.feed()
# animal.move()
# animal.make_noise()
# print()
# print(animal.obj)  # <__main__.Fast object at 0x0000028F6E03B6D0> - объект сейчас
# print(animal.obj.obj)  # <__main__.Predator object at 0x000002592DC3B790> - доступ к предыдущему объекту
# print(animal.obj.obj.obj)  # <__main__.Swimming object at 0x0000015921DBDF70> - доступ к предпредыдущему объекту
# animal.obj.obj = animal.obj.obj.obj  # снятие декораторов (убираем Predator и заменяем предидущим Swimming)
# animal.feed()
# animal.move()
# animal.make_noise()

######################################################################################################################
# Паттерн Адаптер
# Паттерн Адаптер, так же как и декоратор относится к структурным паттернам проектирования. Задача адаптера --
# обеспечение взаимодействия между некоторым базовым класом и адаптируемым классом или группой классов. При этом
# интерфейс адаптируемого объекта может быть не совсестим с интерфейсом базового класса.
# Для обеспечения совместимости создается отдельный класс, который реализует интерфейс взаимодействия с базовым классом
# и использует адаптируемый.
# К структуре паттерна Адаптер относятся только базовый объект, адаптируемый, и сам адаптер.
# Применение паттерна Adapter
# Паттерн адаптер применятся очень часто в огромном количетстве задач. Большое количество библиотек для языка Python
# являются адаптерами к другим библиотркам, написанным на С/С++. Использование подобных оберток позволяет увеличить
# производительность программ на этом языке.
# Кроме библиотек паттерн адаптер часто используется в модулях для работы с базами данных. Это позволяет спрятать
# SQL-код и пользоваться простой и понятной оболочкой.
# Еще адаптеры могут использоваться для сборки большого количества отдельных модулей в единую программу. Проблемы могут
# возникать, когда используются модули от старых проектов или написанные независимыми командами разработчиков и имеют
# несоглосованный интерфейс.
# Стоит отметить, что если есть возможность, интерфейсы следует согласовывать и не использовать паттерн Адаптер. Это
# улучшит читаемость кода, так как в нем не будет лишних сущностей, мешающих пониманию а так же может немного улучшить
# производительность, так как не будет выполняться код собственно паттерна.
# Пример использования адаптера
# import re
# from abc import ABC, abstractmethod
#
# text = '''
# Design Patterns: Elements of Reusable Object-Oriented Software is a software engineering book describing software design
# patterns. The book's authors are Erich Gamma, Richard Helm, Ralph Johnson and John Vlissides with a foreword by
# Grady Booch. The book is divided into two parts, with the first two chapters exploring the capabilities and pitfalls
# of object-oriented programming, and the remaining chapters describing 23 classic software design patterns. The book
# includes examples in C++ and Smalltalk.
# It has been influential to the field of software engineering and is regarded as an important source for object-oriented
# design theory and practice. More than 500,000 copies have been sold in English and in 13 other languages. The authors
#  are often referred to as the Gang of Four (GoF).
# '''
#
#
# class System:  # Класс, представляющий систему
#     def __init__(self, text):
#         tmp = re.sub(r'\W', ' ', text.lower())
#         tmp = re.sub(r' +', ' ', tmp).strip()
#         self.text = tmp
#
#     def get_processed_text(self, processor):  # Метод, требующий на вход класс-обработчик
#         result = processor.process_text(self.text)  # Вызов метода обработчика
#         print(*result, sep='\n')
#
#
# class TextProcessor:  # Абстрактный интерфейс обработчика
#     @abstractmethod
#     def process_text(self, text):
#         pass
#
#
# class WordCounter:  # Обработчик, несовместимый с основной системой
#     def count_words(self, text):
#         self.__words = dict()
#         for word in text.split():
#             self.__words[word] = self.__words.get(word, 0) + 1
#
#     def get_count(self, word):
#         return self.__words.get(word, 0)
#
#     def get_all_words(self):
#         return self.__words.copy()
#
#
# class WordCounterAdapter(TextProcessor):  # Адаптер к обработчику
#     def __init__(self, adaptee):  # В конструкторе указывается, к какому объекту следует подключить адаптер
#         self.adaptee = adaptee
#
#     def process_text(self, text):  # Реализация интерфейса обработчика, требуемого системой.
#         self.adaptee.count_words(text)
#         words = self.adaptee.get_all_words().keys()
#         return sorted(words, key=lambda x: self.adaptee.get_count(x), reverse=True)
#
#
# system = System(text)
# counter = WordCounter()
# adapter = WordCounterAdapter(counter)
# system.get_processed_text(adapter)

######################################################################################################################
# Паттерн Наблюдатель (Observer)
# Паттерн Наблюдатель является поведенческим паттерном проектирования. Он предназначен для организации взаимодействия
# между классами. Он реализует взаимодействия типа один ко многим, при котором множество объектов получают информацию
# об изменениях основного объекта.
# По данному принципу работает огромное количество приложений. Это могут быть новостные рассылки, уведомления от
# приложений на смартфонах, автоматическая рассылка почты, системы достижений в играх и многое другое.
# Вместо решения, при котором объект наблюдатель опрашивает наблюдаемый объект о произошедших изменениях, наблюдаемый
# объект самостоятельно уведомляет о них наблюдателя.
# В паттерне Наблюдатель в наблюдаемой системе должен быть имплементирован интерфейс наблюдаемого объекта, позволяющий
# "подписывать" пользователя на обновления объекта и отправлять всем подписанным пользователям уведомления об
# изменениях. Также должны существовать наблюдатели, реализующие интерфейс наблюдателя.
# Для паттерна Observer необходимы следующие классы:
# - Абстрактный наблюдаемый объект
# - Абстрактный наблюдатель
# - Конкретный наблюдаемый объект
# - Конкретные наблюдатели
# У наблюдаемого объекта должны быть реализованы методы:
# - Подписать наблюдателя на обновления
# - Отписать от обновления
# - Уведомить всех подписчиков об изменениях
# У наблюдателя должен быть реализован метод update, который будет вызван наблюдаемым объектом при обновлении.
# Использование паттерна Наблюдатель
# При использовании паттерна Наблюдатель создаются наблюдатели и система. Для использования паттерна наблюдатель
# подписывается на обновления системы. При изменениях система оповещает об изменениях всех текущих подписчиков при
# помощи вызова у подписчиков метода update.
# Реализация паттерна Наблюдатеь
# from abc import ABC, abstractmethod
#
#
# class NotificationManager:  # Наблюдаемая система
#     def __init__(self):
#         self.__subscribers = set()  # При инициализации множество подписчиков задается пустым
#
#     def subscribe(self, subscriber):
#         self.__subscribers.add(
#             subscriber)  # Для того чтобы подписать пользователя, он добавляется во множество подписчиков
#
#     def unsubcribe(self, subscriber):
#         self.__subscribers.remove(subscriber)  # Удаление подписчика из списка
#
#     def notify(self, message):
#         for subscriber in self.__subscribers:
#             subscriber.update(message)  # Отправка уведомления всем подписчикам
#
#
# class AbstractObserver(ABC):
#     @abstractmethod
#     def update(self, message):  # Абстрактный наблюдатель задает метод update
#         pass
#
#
# class MessageNotifier(AbstractObserver):
#     def __init__(self, name):
#         self.__name = name
#
#     def update(self, message):  # Конкретная реализация метода update
#         print(f'{self.__name} recieved message!')
#
#
# class MessagePrinter(AbstractObserver):
#     def __init__(self, name):
#         self.__name = name
#
#     def update(self, message):  # Конкретная реализация метода update
#         print(f'{self.__name} recieved message: {message}')
#
#
# notifier1 = MessageNotifier("Notifier1")
# printer1 = MessagePrinter("Printer1")
# printer2 = MessagePrinter("Printer2")
#
# manager = NotificationManager()
#
# manager.subscribe(notifier1)
# manager.subscribe(printer1)
# manager.subscribe(printer2)
#
# manager.notify("Hi!")

#######################################################################################################################
# Паттерн "Цепочка обязанностей"
# 1. Описание персонажа
# Опишем персонажа, который будет взаимодействовать с цепочкой обязанностей
class Character:
    def __init__(self):
        self.name = "Nagibator"
        self.xp = 0
        self.passed_quests = set()
        self.taken_quests = set()
# 2. Описание квестов
# Опишем квесты, из которых будет состоять цепочка обязанностей
def add_quest_speak(char):
    quest_name = "Поговорить с фермером"
    xp = 100
    if quest_name not in (char.passed_quests | char.taken_quests):
        print(f"Квест получен: \"{quest_name}\"")
        char.taken_quests.add(quest_name)
    elif quest_name in char.taken_quests:
        print(f"Квест сдан: \"{quest_name}\"")
        char.passed_quests.add(quest_name)
        char.taken_quests.remove(quest_name)
        char.xp += xp


def add_quest_hunt(char):
    quest_name = "Охота на крыс"
    xp = 300
    if quest_name not in (char.passed_quests | char.taken_quests):
        print(f"Квест получен: \"{quest_name}\"")
        char.taken_quests.add(quest_name)
    elif quest_name in char.taken_quests:
        print(f"Квест сдан: \"{quest_name}\"")
        char.passed_quests.add(quest_name)
        char.taken_quests.remove(quest_name)
        char.xp += xp


def add_quest_carry(char):
    quest_name = "Принести доски из сарая"
    xp = 200
    if quest_name not in (char.passed_quests | char.taken_quests):
        print(f"Квест получен: \"{quest_name}\"")
        char.taken_quests.add(quest_name)
    elif quest_name in char.taken_quests:
        print(f"Квест сдан: \"{quest_name}\"")
        char.passed_quests.add(quest_name)
        char.taken_quests.remove(quest_name)
        char.xp += xp
# 3. Описание квестгивера
# Опишем персонажа, который будет давать игрокам квесты. У него определим список доступных квестов, который можно
# пополнять.
# Определим метод handle_quests, который позволяет применить квест к персонажу.
class QuestGiver:
    def __init__(self):
        self.quests = []

    def add_quest(self, quest):
        self.quests.append(quest)

    def handle_quests(self, character):
        for quest in self.quests:
            quest(character)
# 4. Применение цепочки обязанностей
# Создадим квестгивера и передадим ему все квесты, которые он может давать и принимать.
all_quests = [add_quest_speak, add_quest_hunt, add_quest_carry]

quest_giver = QuestGiver()

for quest in all_quests:
    quest_giver.add_quest(quest)

player = Character()
# Персонаж подходит к квестгиверу и берет квесты
quest_giver.handle_quests(player)
# Квест получен: "Поговорить с фермером"
# Квест получен: "Охота на крыс"
# Квест получен: "Принести доски из сарая"
# Проверим, какие квесты активны на данный момент
print("Получено: ", player.taken_quests)
print("Сдано: ", player.passed_quests)
# Получено:  {'Принести доски из сарая', 'Поговорить с фермером', 'Охота на крыс'}
# Сдано:  set()
# Изменим полученные квесты

player.taken_quests = {'Принести доски из сарая', 'Поговорить с фермером'}
# Подойдем к квестгиверу еще раз

quest_giver.handle_quests(player)
# Квест сдан: "Поговорить с фермером"
# Квест получен: "Охота на крыс"
# Квест сдан: "Принести доски из сарая"
print("Получено: ", player.taken_quests)
print("Сдано: ", player.passed_quests)
# Получено:  {'Охота на крыс'}
# Сдано:  {'Поговорить с фермером', 'Принести доски из сарая'}
# Сдадим оставшийся квест и проверим состояние

quest_giver.handle_quests(player)
# Квест сдан: "Охота на крыс"
print("Получено: ", player.taken_quests)
print("Сдано: ", player.passed_quests)
# Получено:  set()
# Сдано:  {'Поговорить с фермером', 'Принести доски из сарая', 'Охота на крыс'}


# Паттерн "Цепочка обязанностей"
# 1. Объявление возможных типов событий
QUEST_SPEAK, QUEST_HUNT, QUEST_CARRY = "QSPEAK", "QHUNT", "QCARRY"
# 2. Описание персонажа
# Опишем персонажа, который будет взаимодействовать с цепочкой обязанностей
class Character:

    def __init__(self):
        self.name = "Nagibator"
        self.xp = 0
        self.passed_quests = set()
        self.taken_quests = set()
# 3. Опишем класс события
# При возникновении определенного события запускается цепочка обязанностей, которая может это событие обрабатывать
class Event:

    def __init__(self, kind):
        self.kind = kind
# 4. Опишем базовое звено цепочки обязанностей
# Элементарный обработчик просто передает событие следующему звену цепочки, если таковое имеется.
class NullHandler:

    def __init__(self, successor=None):
        self.__successor = successor

    def handle(self, char, event):
        if self.__successor is not None:
            self.__successor.handle(char, event)
# 5. Опишем обработчики квестов
# Для каждого квеста напишем обработчик и определим событие, при котором этот обработчик будет срабатывать.
class HandleQSpeak(NullHandler):

    def handle(self, char, event):
        if event.kind == QUEST_SPEAK:
            xp = 100
            quest_name = "Поговорить с фермером"
            if event.kind not in (char.passed_quests | char.taken_quests):
                print(f"Квест получен: \"{quest_name}\"")
                char.taken_quests.add(event.kind)
            elif event.kind in char.taken_quests:
                print(f"Квест сдан: \"{quest_name}\"")
                char.passed_quests.add(event.kind)
                char.taken_quests.remove(event.kind)
                char.xp += xp
        else:
            print("Передаю обработку дальше")
            super().handle(char, event)


class HandleQHunt(NullHandler):

    def handle(self, char, event):
        if event.kind == QUEST_HUNT:
            xp = 300
            quest_name = "Охота на крыс"
            if event.kind not in (char.passed_quests | char.taken_quests):
                print(f"Квест получен: \"{quest_name}\"")
                char.taken_quests.add(event.kind)
            elif event.kind in char.taken_quests:
                print(f"Квест сдан: \"{quest_name}\"")
                char.passed_quests.add(event.kind)
                char.taken_quests.remove(event.kind)
                char.xp += xp
        else:
            print("Передаю обработку дальше")
            super().handle(char, event)


class HandleQCarry(NullHandler):

    def handle(self, char, event):
        if event.kind == QUEST_CARRY:
            xp = 200
            quest_name = "Принести дрова из сарая"
            if event.kind not in (char.passed_quests | char.taken_quests):
                print(f"Квест получен: \"{quest_name}\"")
                char.taken_quests.add(event.kind)
            elif event.kind in char.taken_quests:
                print(f"Квест сдан: \"{quest_name}\"")
                char.passed_quests.add(event.kind)
                char.taken_quests.remove(event.kind)
                char.xp += xp
        else:
            print("Передаю обработку дальше")
            super().handle(char, event)
# 6. Опишем квестгивера
# Квестгивер будет хранить цепочку обработчиков и список событий, на которые он может реагировать. Список событий можно
# пополнять.
# Метод handle_quests генерирует все доступные события и передает их на обработку цепочке.
class QuestGiver:

    def __init__(self):
        self.handlers = HandleQSpeak(HandleQHunt(HandleQCarry(NullHandler())))
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def handle_quests(self, char):
        for event in self.events:
            self.handlers.handle(char, event)
# 7. Создадим квестгивера и дадим ему все возможные события
events = [Event(QUEST_CARRY), Event(QUEST_HUNT), Event(QUEST_SPEAK)]

quest_giver = QuestGiver()

for event in events:
    quest_giver.add_event(event)
# 8. Проверим работы цепочки обязанностейй на примере, аналогичном предыдущему
player = Character()

quest_giver.handle_quests(player)
print()
player.taken_quests = {QUEST_CARRY, QUEST_SPEAK}
quest_giver.handle_quests(player)
print()
quest_giver.handle_quests(player)
# Передаю обработку дальше
# Передаю обработку дальше
# Квест получен: "Принести дрова из сарая"
# Передаю обработку дальше
# Квест получен: "Охота на крыс"
# Квест получен: "Поговорить с фермером"
#
# Передаю обработку дальше
# Передаю обработку дальше
# Квест сдан: "Принести дрова из сарая"
# Передаю обработку дальше
# Квест получен: "Охота на крыс"
# Квест сдан: "Поговорить с фермером"
#
# Передаю обработку дальше
# Передаю обработку дальше
# Передаю обработку дальше
# Квест сдан: "Охота на крыс"
# Видно, что цепочка обязанностей работает, и квесты, обработка которых невозможна на данном этапе, передаются по ней
# дальше

######################################################################################################################
# Паттерн "Абстрактная фабрика"
# Импортируем необходимые классы и методы
from abc import ABC, abstractmethod
# 1. Объявим абстрактый класс фабрики
# Обявим методы, которые позволят создать персонажа, а также оружие и заклинание для него.
class HeroFactory(ABC):
    @abstractmethod
    def create_hero(self, name):
        pass

    @abstractmethod
    def create_weapon(self):
        pass

    @abstractmethod
    def create_spell(self):
        pass
# 2. Определим конкретные фабрики
# Оределим конкретные фабрики и необходимые классы, для каждого из классов персонажей
class WarriorFactory(HeroFactory):
    def create_hero(self, name):
        return Warrior(name)

    def create_weapon(self):
        return Claymore()

    def create_spell(self):
        return Power()


class Warrior:
    def __init__(self, name):
        self.name = name
        self.weapon = None
        self.armor = None
        self.spell = None

    def add_weapon(self, weapon):
        self.weapon = weapon

    def add_spell(self, spell):
        self.spell = spell

    def hit(self):
        print(f"Warrior {self.name} hits with {self.weapon.hit()}")
        self.weapon.hit()

    def cast(self):
        print(f"Warrior {self.name} casts {self.spell.cast()}")
        self.spell.cast()


class Claymore:
    def hit(self):
        return "Claymore"


class Power:
    def cast(self):
        return "Power"


class MageFactory(HeroFactory):
    def create_hero(self, name):
        return Mage(name)

    def create_weapon(self):
        return Staff()

    def create_spell(self):
        return Fireball()


class Mage:
    def __init__(self, name):
        self.name = name
        self.weapon = None
        self.armor = None
        self.spell = None

    def add_weapon(self, weapon):
        self.weapon = weapon

    def add_spell(self, spell):
        self.spell = spell

    def hit(self):
        print(f"Mage {self.name} hits with {self.weapon.hit()}")
        self.weapon.hit()

    def cast(self):
        print(f"Mage {self.name} casts {self.spell.cast()}")
        self.spell.cast()


class Staff:
    def hit(self):
        return "Staff"


class Fireball:
    def cast(self):
        return "Fireball"


class AssassinFactory(HeroFactory):
    def create_hero(self, name):
        return Assassin(name)

    def create_weapon(self):
        return Dagger()

    def create_spell(self):
        return Invisibility()


class Assassin:
    def __init__(self, name):
        self.name = name
        self.weapon = None
        self.armor = None
        self.spell = None

    def add_weapon(self, weapon):
        self.weapon = weapon

    def add_spell(self, spell):
        self.spell = spell

    def hit(self):
        print(f"Assassin {self.name} hits with {self.weapon.hit()}")
        self.weapon.hit()

    def cast(self):
        print(f"Assassin {self.name} casts {self.spell.cast()}")


class Dagger:
    def hit(self):
        return "Dagger"


class Invisibility:
    def cast(self):
        return "Invisibility"
# 3. Определим функцию, создающую персонажей
# Определим функцию, зависящую от фабрики. Данная функция будет создавать прсонажа и его экипировку в зависимости от
# фабрики, которая будет передаваться в качестве аргумента.
def create_hero(factory):
    hero = factory.create_hero("Nagibator")

    weapon = factory.create_weapon()
    ability = factory.create_spell()

    hero.add_weapon(weapon)
    hero.add_spell(ability)

    return hero
# 4. Попробуем создать персонажей различных классов
# Попробуем создать персонажей различных классов, передавая функции назличные фабрики.
factory = AssassinFactory()
player = create_hero(factory)
player.cast()
player.hit()
# Assassin Nagibator casts Invisibility
# Assassin Nagibator hits with Dagger
factory = MageFactory()
player = create_hero(factory)
player.cast()
player.hit()
# Mage Nagibator casts Fireball
# Mage Nagibator hits with Staff

# Паттерн "Абстрактная фабрика"
# 1. Объявим абстрактную фабрику
# Обявим методы, которые позволят создать персонажа. Используем механизм classmethod
class HeroFactory:
    @classmethod
    def create_hero(Class, name):
        return Class.Hero(name)

    @classmethod
    def create_weapon(Class):
        return Class.Weapon()

    @classmethod
    def create_spell(Class):
        return Class.Spell()
# 2. Определим конкретные фабрики
# В каждой конкретной фабрике объявим собственные классы героя, оружия и заклинаний, которые будут специфичны для класса
# персонажа
class WariorFactory(HeroFactory):
    class Hero:
        def __init__(self, name):
            self.name = name
            self.weapon = None
            self.armor = None
            self.spell = None

        def add_weapon(self, weapon):
            self.weapon = weapon

        def add_spell(self, spell):
            self.spell = spell

        def hit(self):
            print(f"Warior hits with {self.weapon.hit()}")
            self.weapon.hit()

        def cast(self):
            print(f"Warior casts {self.spell.cast()}")
            self.spell.cast()

    class Weapon:
        def hit(self):
            return "Claymore"

    class Spell:
        def cast(self):
            return "Power"


class MageFactory(HeroFactory):
    class Hero:
        def __init__(self, name):
            self.name = name
            self.weapon = None
            self.armor = None
            self.spell = None

        def add_weapon(self, weapon):
            self.weapon = weapon

        def add_spell(self, spell):
            self.spell = spell

        def hit(self):
            print(f"Mage hits with {self.weapon.hit()}")
            self.weapon.hit()

        def cast(self):
            print(f"Mage casts {self.spell.cast()}")
            self.spell.cast()

    class Weapon:
        def hit(self):
            return "Staff"

    class Spell:
        def cast(self):
            return "Fireball"


class AssassinFactory(HeroFactory):
    class Hero:
        def __init__(self, name):
            self.name = name
            self.weapon = None
            self.armor = None
            self.spell = None

        def add_weapon(self, weapon):
            self.weapon = weapon

        def add_spell(self, spell):
            self.spell = spell

        def hit(self):
            print(f"Assassin hits with {self.weapon.hit()}")
            self.weapon.hit()

        def cast(self):
            print(f"Assassin casts {self.spell.cast()}")

    class Weapon:
        def hit(self):
            return "Dagger"

    class Spell:
        def cast(self):
            return "Invisibility"
# 3. Определим функцию, создающую персонажей
# Она не отличается от базовой реализации
def create_hero(factory):
    hero = factory.create_hero("Nagibator")

    weapon = factory.create_weapon()
    spell = factory.create_spell()

    hero.add_weapon(weapon)
    hero.add_spell(spell)

    return hero
# 4. Попробуем создать персонажей различных классов
# Попробуем создать персонажей различных классов, передавая функции назличные фабрики.
player = create_hero(AssassinFactory)
player.cast()
player.hit()
# Assassin casts Invisibility
# Assassin hits with Dagger
player = create_hero(MageFactory)
player.cast()
player.hit()
# Mage casts Fireball
# Mage hits with Staff

######################################################################################################################
# Конфигурирование с YAML
# В данном примере будет показано, как можно сконфигурировать отчёт при помощи YAML файла.
# В качестве фабрики, по производству отчёта возмём фабрики, созданные в предыдущих уроках, но изменим их так, чтобы
# формирование отчёта осуществялось через загрузку yaml файла.
# YAML файл отчёта
# Определим строковые переменные yml_MD и yml_HTML в которых будут храниться содержание конфигурационных фалов для
# Markdown и HTML отчёта соответственно.
# для Markdown отчёта
yml_MD = '''
--- !MDreport                # указывает, что хранящаяся ниже структура относиться к типу MDreport   
objects:                     # для хранения якорей
  - &img !img                # якорь img хранит объект типа img
      alt_text: coursera     # описание изображения
      src: "https://blog.coursera.org/wp-content/uploads/2017/07/coursera-fb.png"   # адрес изображения
report: !report              # содержит непосредственно отчёт
  filename: report_yaml.md   # имя файла отчёта
  title: !!str Report        # название отчёта - строковый параметр (!!str) "Report"
  parts:                     # содержание отчёта - список частей (каждая часть начинаеться с "-")
    - !chapter                   # первая часть отчёта - объект типа "chapter"
      caption: "chapter one"         # заглавие первой части
      parts:                         # содержание первой части - список ниже

 # первая часть - текст.
 # символ '>' вконце показывает, что весь блок ниже являеться содержанием. Перенос строк не учитываеться
 # Для учёта переноса строк - символ '|'

        - |                            
          chapter
          1
          text               
        - !link                          # далее ссылка
            obj: coursera                    # текст ссылки
            href: "https://ru.coursera.org"  # куда ссылаеться
    - !chapter                   # вторая часть отчёта - объект типа "chapter"
      caption: "chapter two"         # заглавие второй части
      parts:                         # содержание второй части - список ниже
        - "Chapter 2 header"             # сначала текст
        - !link                          # далее ссылка
            obj: *img                        # объект, хранящийся по якорю img (изображение) будет являться ссылкой
            href: "https://ru.coursera.org"  # куда ссылаеться
        - "Chapter 2 footer"             # в конце - текст'''
# Для HTML отчёта только одно изминение — тип отчёта:
yml_HTML = '''
--- !HTMLreport             # указывает, что хранящаяся ниже структура относиться к типу HTMLreport
objects:
  - &img !img
      alt_text: google
      src: "https://blog.coursera.org/wp-content/uploads/2017/07/coursera-fb.png"
report: !report
  filename: report_yaml.html
  title: Report
  parts:
    - !chapter
      caption: "chapter one"
      parts:
        - "chapter 1 text"
        - !link
            obj: coursera
            href: "https://ru.coursera.org"
    - !chapter
      caption: "chapter two"
      parts:
        - "Chapter 2 header"
        - !link
            obj: *img
            href: "https://ru.coursera.org"
        - "Chapter 2 footer"'''
# Далее перейдём к изменению абстрактной фабрики ReportFactory
import yaml      # для работы с PyYAML


# теперь ReportFactory - потомок yaml.YAMLObject.
# Сделано для того, чтобы yaml оработчик знал новый тип данных, указанный в yaml_tag
# он будет определён в фабриках - потомках
class ReportFactory(yaml.YAMLObject):

    # данные yaml фала - структура отчёта одинакова для всех потомков.
    # В связи с этим - получение отчёта из yaml файла - классовый метод со специальным именем from_yaml
    @classmethod
    def from_yaml(Class, loader, node):
        # сначала опишем функции для обработки каждого нового типа
        # метод loader.construct_mapping() формирует из содержания node словарь

        # обработчик создания отчёта !report
        def get_report(loader, node):
            data = loader.construct_mapping(node)
            rep = Class.make_report(data["title"])
            rep.filename = data["filename"]
            # на данный момент data["parts"] пуст. Он будет заполнен позже, соответствующим обработчиком,
            # сохраняем на него ссылку, дополнив сразу частями из rep.parts
            data["parts"].extend(rep.parts)
            rep.parts = data["parts"]
            return rep

    # обработчик создания части !chapter
        def get_chapter(loader, node):
            data = loader.construct_mapping(node)
            ch = Class.make_chapter(data["caption"])
            # аналогично предыдущему обработчику
            data["parts"].extend(ch.objects)
            ch.objects = data["parts"]
            return ch

    # обработчик создания ссылки !link
        def get_link(loader, node):
            data = loader.construct_mapping(node)
            lnk = Class.make_link(data["obj"], data["href"])
            return lnk

    # обработчик создания изображения !img
        def get_img(loader, node):
            data = loader.construct_mapping(node)
            img = Class.make_img(data["alt_text"], data["src"])
            return img

    # добавляем обработчики
        loader.add_constructor(u"!report", get_report)
        loader.add_constructor(u"!chapter", get_chapter)
        loader.add_constructor(u"!link", get_link)
        loader.add_constructor(u"!img", get_img)

    # возвращаем результат yaml обработчика - отчёт
        return loader.construct_mapping(node)['report']

    # ниже - без изменений

    @classmethod
    def make_report(Class, title):
        return Class.Report(title)

    @classmethod
    def make_chapter(Class, caption):
        return Class.Chapter(caption)

    @classmethod
    def make_link(Class, obj, href):
        return Class.Link(obj, href)

    @classmethod
    def make_img(Class, alt_text, src):
        return Class.Img(alt_text, src)
# Далее берём непосредственно фабрики по производству элементов отчёта. Добавляем соответствие фабрик yaml типу
class MDreportFactory(ReportFactory):
    yaml_tag = u'!MDreport'        # указываем соответствие

    class Report:
        def __init__(self, title):
            self.parts = []
            self.parts.append("# "+title+"\n\n")

        def add(self, part):
            self.parts.append(part)

        def save(self):          # вносим изменения - имя файла отчёта указываеться в yaml файле
            try:
                file = open(self.filename, "w", encoding="utf-8")
                print('\n'.join(map(str, self.parts)), file=file)
            finally:
                if isinstance(self.filename, str) and file is not None:
                    file.close()

    class Chapter:
        def __init__(self, caption):
            self.caption = caption
            self.objects = []

        def add(self, obj):
            print(obj)
            self.objects.append(obj)

        def __str__(self):
            return f'## {self.caption}\n\n' + ''.join(map(str, self.objects))

    class Link:
        def __init__(self, obj, href):
            self.obj = obj
            self.href = href

        def __str__(self):
            return f'[{self.obj}]({self.href})'

    class Img:
        def __init__(self, alt_text, src):
            self.alt_text = alt_text
            self.src = src

        def __str__(self):
            return f'![{self.alt_text}]({self.src})'


class HTMLreportFactory(ReportFactory):
    yaml_tag = u'!HTMLreport'

    class Report:
        def __init__(self, title):
            self.title = title
            self.parts = []
            self.parts.append("<html>")
            self.parts.append("<head>")
            self.parts.append("<title>" + title + "</title>")
            self.parts.append("<meta charset=\"utf-8\">")
            self.parts.append("</head>")
            self.parts.append("<body>")

        def add(self, part):
            self.parts.append(part)

        def save(self):
            try:
                file = open(self.filename, "w", encoding="utf-8")
                print('\n'.join(map(str, self.parts)), file=file)
            finally:
                if isinstance(self.filename, str) and file is not None:
                    file.close()

    class Chapter:
        def __init__(self, caption):
            self.caption = caption
            self.objects = []

        def add(self, obj):
            self.objects.append(obj)

        def __str__(self):
            ch = f'<h1>{self.caption}</h1>'
            return ch + ''.join(map(str, self.objects))

    class Link:
        def __init__(self, obj, href):
            self.obj = obj
            self.href = href

        def __str__(self):
            return f'<a href="{self.href}">{self.obj}</a>'

    class Img:
        def __init__(self, alt_text, src):
            self.alt_text = alt_text
            self.src = src

        def __str__(self):
            return f'<img alt = "{self.alt_text}", sr c ="{self.src}"/>'
# Осталось провести загрузку yaml файла и вывести результат
from IPython.display import display, Markdown, HTML

txtreport = yaml.load(yml_MD)            # загружаем yaml файл markdown отчёта
txtreport.save()                         # сохраняем
print("Сохранено:", txtreport.filename)  # вывод

HTMLreport = yaml.load(yml_HTML)         # загружаем yaml файл markdown отчёта
HTMLreport.save()                        # сохраняем
print("Сохранено:", HTMLreport.filename)  # вывод

# Выводим результат работы в jupyter notebook

display(Markdown('# <span style="color:red">report.md</span>'))
display(Markdown(filename="report_yaml.md"))
display(Markdown('# <span style="color:red">report.html</span>'))
display(HTML(filename="report_yaml.html"))
# Сохранено: report_yaml.md
# Сохранено: report_yaml.html
# <IPython.core.display.Markdown object>
# <IPython.core.display.Markdown object>
# <IPython.core.display.Markdown object>
# Report

# У меня проблемы с пониманием процесса создания объектов с использованием yaml, не могли бы вы пояснить? А то совсем
# запутался.
# Постараюсь коротко пояснить. Когда происходит загрузка (по существу создание объектов на основании yaml), используются
# уже определенные конструкторы типов данных (например: для списков, чисел , словарей). Если мы определили свой класс в
# коде, то мы не сможем использовать указание на него в yaml файле, так конструктор для него отсутствует.  Для
# исправления этой ситуации возможны два варианта:
# первый - не изменяя определения пользовательского класса (не внося изменения в код нашего класса), определить функцию
# конструктор, которая будет загружать данные и на основе их создавать экземпляр необходимого типа данных и возвращать
# его. Далее, эту созданную функцию нужно зарегистрировать (добавить к существующим конструкторам) с помощью функции
# add_constructor.
# второй - добавить в реализацию класса нужного нам типа данных (в код нашего класса), атрибут класса yaml_tag и метод
# класса с названием from_yaml, который по существу делает тоже самое, что и функция конструктор из первого варианта.
# При этом нужно соблюсти еще одно условие - класс должен наследоваться от  yaml.YAMLObject.
# Вот пара примеров:
# демонстрация загрузки yaml по первому варианту
# важное замечание версия PyYAML - 3.13
import yaml


# класс определяющий пользовательский тип данных
class ExampleClass:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'ExampleClass, value - {self.value}'


# функция конструктор для типа данных ExampleClass
def constuctor_example_class(loader, node):
    # получаем данные из yaml
    value = loader.construct_mapping(node)
    # необходимо выбрать из полученные данных необходимые
    # для создания экземпляра класса ExampleClass
    return ExampleClass(*value)


# регистрируем конструктор
yaml.add_constructor('!example_class', constuctor_example_class)
# yaml строка
document = """!example_class {5}"""
# выполняем загрузку
obj = yaml.load(document)
# выведем полученный объект, ожидаем строку
# ExampleClass, value - 5


# демонстрация загрузки yaml по второму варианту ###############################################################
# важное замечание версия PyYAML - 3.13
import yaml

# класс определяющий пользовательский тип данных
class ExampleClass(yaml.YAMLObject):  # <-- добавим родительский класс yaml.YAMLObject
    yaml_tag = '!example_class'  # <-- добавим тег

    @classmethod
    def from_yaml(cls, loader, node):  # <-- добавим метод класса from_yaml
        # получаем данные из yaml
        value = loader.construct_mapping(node)
        # необходимо выбрать из полученные данных необходимые
        # для создания экземпляра класса ExampleClass
        return ExampleClass(*value)

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'ExampleClass, value - {self.value}'


# yaml строка
document = """!example_class {7}"""
# выполняем загрузку
obj = yaml.load(document)
# выведем полученный объект, ожидаем строку
# ExampleClass, value - 7
print(obj)


