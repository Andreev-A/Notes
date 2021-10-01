# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd
sd.resolution = (450, 500)
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# TODO здесь ваш код
# x_1 = 50
# x_2 = 350
# for color in rainbow_colors:
#     point_1 = sd.get_point(x_1, 50)
#     point_2 = sd.get_point(x_2, 450)
#     sd.line(start_point=point_1, end_point=point_2, color=color, width=4)
#     x_1 += 5
#     x_2 += 5
# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

point = sd.get_point(350, -200)
radius = 450
for color in rainbow_colors:
    sd.circle(center_position=point, radius=radius, color=color, width=14)
    radius += 15

sd.pause()