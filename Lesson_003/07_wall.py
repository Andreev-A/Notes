# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
sd.resolution = (1200, 600)
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
color = sd.COLOR_DARK_YELLOW
length, height = 100, 50
row = 0
for y in range(0, sd.resolution[1], height):
    row += 1
    for x in range(0, sd.resolution[0], length):
        x_0 = x if row % 2 else x + length // 2
        left_bottom = sd.get_point(x_0, y)
        right_top = sd.get_point(x_0 + length, y + height)
        sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=color,  width=2)

sd.pause()



