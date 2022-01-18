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




