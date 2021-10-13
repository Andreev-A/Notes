# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
sd.resolution = (1200, 600)
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
color = sd.COLOR_DARK_YELLOW
y_0 = 0
for i in range(12):
    x_0 = 0 if i % 2 else 50
    for j in range(12):
        point_0 = sd.get_point(x_0, y_0)
        point_1 = sd.get_point(x_0 + 100, y_0 + 50)
        sd.rectangle(left_bottom=point_0, right_top=point_1, color=color,  width=2)
        x_0 += 100
    y_0 += 50
sd.pause()


