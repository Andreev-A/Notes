# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw
simple_draw.resolution = (1200, 600)
# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

# TODO здесь ваш код
color = simple_draw.COLOR_DARK_YELLOW

# x, y = simple_draw.random_point()
# x, y = 0, 0

point_0 = simple_draw.random_point()
point_1 = simple_draw.get_point(point_0 + 100, point_0 + 50)
simple_draw.ellipse(left_bottom=point_0, right_top=point_1, color=color, width=2)
# sd.circle(center_position=point, radius=radius, width=2)

# random.randint(2, 10)

simple_draw.pause()
