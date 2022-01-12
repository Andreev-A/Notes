# Представьте себя ненадолго разработчиком компьютерной игры в стиле фэнтези. Вам поручено написать реализацию системы
# эффектов, которые могут быть наложены на героя вашей игры.
# В игре есть герой, который обладает некоторым набором характеристик. Класс героя Hero.
# К основным характеристикам относятся: Сила (Strength), Восприятие (Perception), Выносливость (Endurance),
# Харизма (Charisma), Интеллект (Intelligence), Ловкость (Agility), Удача (Luck).
# Враги и союзники могут накладывать на героя положительные и отрицательные эффекты. Эти эффекты изменяют характеристики
# героя,  увеличивая или уменьшая значения определенных характеристик, в зависимости от того какие эффекты были наложены
# На героя можно накладывать бесконечно много эффектов, действие одинаковых эффектов суммируется. Игрок должен знать,
# какие положительные и какие отрицательные эффекты на него были наложены и в каком порядке. Названия эффектов совпадают
# с названиями классов.
# За получение данных о текущем состоянии героя отвечают методы get_stats, get_positive_effects,  get_negative_effects.
# Описание эффектов:
# Берсерк (Berserk) -
# Увеличивает характеристики: Сила, Выносливость, Ловкость, Удача на 7;
# уменьшает характеристики: Восприятие, Харизма, Интеллект на 3;
# количество единиц здоровья увеличивается на 50.
# Благословение (Blessing) -
# увеличивает все основные характеристики на 2.
# Слабость (Weakness) -
# уменьшает характеристики: Сила, Выносливость, Ловкость на 4.
# Сглаз (EvilEye) -
# уменьшает  характеристику Удача на 10.
# Проклятье (Curse) -
# уменьшает все основные характеристики на 2.
# При выполнении задания необходимо учитывать, что:
# изначальные характеристики базового объекта не должны меняться.
# изменения характеристик и накладываемых эффектов (баффов/дебаффов) должны происходить динамически, то есть вычисляться
# при вызове методов get_stats, get_positive_effects, get_negative_effects
# абстрактные классы AbstractPositive,  AbstractNegative и соответственно их потомки могут принимать любой параметр base
# при инициализации объекта (_ _ init _ _ (self, base))
# эффекты должны корректно сниматься, в том числе и из середины стека
# Для тестирования правильности работы вашего решения вы можете повторить пример работы, приведенный ниже, или
# использовать тестовый скрипт.  Заметим, что данные примеры не покрывают всех тестовых случаев, проверяемых тестовой
# системой, это всего лишь отправная точка для ваших экспериментов с кодом решения.

####################################################################################################################
from abc import ABC, abstractmethod


class Hero:
    def __init__(self):
        self.positive_effects = []
        self.negative_effects = []
        self.stats = {
            "HP": 128,  # health points
            "MP": 42,  # magic points,
            "SP": 100,  # skill points
            "Strength": 15,  # сила
            "Perception": 4,  # восприятие
            "Endurance": 8,  # выносливость
            "Charisma": 2,  # харизма
            "Intelligence": 3,  # интеллект
            "Agility": 8,  # ловкость
            "Luck": 1  # удача
        }

    def get_positive_effects(self):
        return self.positive_effects.copy()

    def get_negative_effects(self):
        return self.negative_effects.copy()

    def get_stats(self):
        return self.stats.copy()


class AbstractEffect(Hero, ABC):
    def __init__(self, base):
        super().__init__()
        self.base = base

    @abstractmethod
    def get_positive_effects(self):
        pass

    @abstractmethod
    def get_negative_effects(self):
        pass

    @abstractmethod
    def get_stats(self):
        pass


class AbstractPositive(AbstractEffect):
    def get_negative_effects(self):
        return self.base.get_negative_effects()


class AbstractNegative(AbstractEffect):
    def get_positive_effects(self):
        return self.base.get_positive_effects()


class Berserk(AbstractPositive):
    def get_stats(self):
        stats = self.base.get_stats()
        stats["HP"] += 50
        stats["Strength"] += 7
        stats["Endurance"] += 7
        stats["Agility"] += 7
        stats["Luck"] += 7
        stats["Perception"] -= 3
        stats["Charisma"] -= 3
        stats["Intelligence"] -= 3
        return stats

    def get_positive_effects(self):
        return self.base.get_positive_effects() + ['Berserk']


class Blessing(AbstractPositive):
    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] += 2
        stats["Endurance"] += 2
        stats["Agility"] += 2
        stats["Luck"] += 2
        stats["Perception"] += 2
        stats["Charisma"] += 2
        stats["Intelligence"] += 2
        return stats

    def get_positive_effects(self):
        return self.base.get_positive_effects() + ['Blessing']


class Weakness(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] -= 4
        stats["Endurance"] -= 4
        stats["Agility"] -= 4
        return stats

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ['Weakness']


class EvilEye(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        stats["Luck"] -= 10
        return stats

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ['EvilEye']


class Curse(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] -= 2
        stats["Endurance"] -= 2
        stats["Agility"] -= 2
        stats["Luck"] -= 2
        stats["Perception"] -= 2
        stats["Charisma"] -= 2
        stats["Intelligence"] -= 2
        return stats

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ['Curse']


# hero = Hero()
# print(hero.get_stats())
# print(hero.get_negative_effects())
# print(hero.get_positive_effects())
# print('---------------')
# brs1 = Berserk(hero)
# print(brs1.get_stats())
# print(brs1.get_negative_effects())
# print(brs1.get_positive_effects())
# print('---------------')
# brs2 = Berserk(brs1)
# print(brs2.get_stats())
# print(brs2.get_negative_effects())
# print(brs2.get_positive_effects())
# print('---------------')
# cur1 = Curse(brs2)
# print(cur1.get_stats())
# print(cur1.get_negative_effects())
# print(cur1.get_positive_effects())
# print('---------------')
# cur1.base = brs1
# print(cur1.get_stats())
# print(cur1.get_negative_effects())
# print(cur1.get_positive_effects())

######################################################################################################################
# Создание декоратора класса — решение
######################################################################################################################
# Объявим абстрактный декоратор
class AbstractEffect(Hero, ABC):

    def __init__(self, base):
        self.base = base

    @abstractmethod
    def get_positive_effects(self):
        return self.positive_effects

    @abstractmethod
    def get_negative_effects(self):
        return self.negative_effects

    @abstractmethod
    def get_stats(self):
        pass


# В AbstractPositive будем возвращать список наложенных отрицательных эффектов без изменений, чтобы не определять данный
# метод во всех положительных эффектах
class AbstractPositive(AbstractEffect):

    def get_negative_effects(self):
        return self.base.get_negative_effects()


# Объявим несколько положительных эффектов
class Berserk(AbstractPositive):

    def get_stats(self):
        # Получим характеристики базового объекта, модифицируем их и вернем
        stats = self.base.get_stats()
        stats["HP"] += 50
        stats["Strength"] += 7
        stats["Endurance"] += 7
        stats["Agility"] += 7
        stats["Luck"] += 7
        stats["Perception"] -= 3
        stats["Charisma"] -= 3
        stats["Intelligence"] -= 3
        return stats

    def get_positive_effects(self):
        # Модифицируем список эффектов, добавив в него новый эффект
        return self.base.get_positive_effects() + ["Berserk"]


class Blessing(AbstractPositive):

    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] += 2
        stats["Endurance"] += 2
        stats["Agility"] += 2
        stats["Luck"] += 2
        stats["Perception"] += 2
        stats["Charisma"] += 2
        stats["Intelligence"] += 2
        return stats

    def get_positive_effects(self):
        return self.base.get_positive_effects() + ["Blessing"]


# Для отрицательных эффектов неизменным останется список положительных эффектов
class AbstractNegative(AbstractEffect):

    def get_positive_effects(self):
        return self.base.get_positive_effects()


# Аналогично положительным эффектам, объявим отрицательные
class Weakness(AbstractNegative):

    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] -= 4
        stats["Endurance"] -= 4
        stats["Agility"] -= 4
        return stats

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["Weakness"]


class Curse(AbstractNegative):

    def get_stats(self):
        stats = self.base.get_stats()
        stats["Strength"] -= 2
        stats["Endurance"] -= 2
        stats["Agility"] -= 2
        stats["Luck"] -= 2
        stats["Perception"] -= 2
        stats["Charisma"] -= 2
        stats["Intelligence"] -= 2
        return stats

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["Curse"]


class EvilEye(AbstractNegative):

    def get_stats(self):
        stats = self.base.get_stats()
        stats["Luck"] -= 10
        return stats

    def get_negative_effects(self):
        return self.base.get_negative_effects() + ["EvilEye"]

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
