# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join


from district.central_street.house1.room1 import folks as room1
from district.central_street.house1.room2 import folks as room2
from district.central_street.house2.room1 import folks as room3
from district.central_street.house2.room2 import folks as room4
from district.soviet_street.house1.room1 import folks as room5
from district.soviet_street.house1.room2 import folks as room6
from district.soviet_street.house2.room1 import folks as room7
from district.soviet_street.house2.room2 import folks as room8

my_print = room1 + room2 + room3 + room4 + room5 + room6 + room7 + room8
print('На районе живут: ' + ', '.join(map(str, my_print)))
