# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

import my_burger

recipe = []
print('Давйте создадим рецепт бургера. Итак начнем')
my_burger.add_buns(recipe)
my_burger.add_cutlets(recipe)
my_burger.add_cucumber(recipe)
my_burger.add_tomato(recipe)
my_burger.add_sauce(recipe)
my_burger.add_mayonnaise(recipe)
my_burger.add_cheese(recipe)
print('Получился следующий рецепт: ' + ", ".join(map(str, recipe)))
