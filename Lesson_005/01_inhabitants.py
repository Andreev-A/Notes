# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

from room_1 import folks
from room_2 import folks as folks_2

print('В комнате room_1 живут: ' + ", ".join(map(str, folks)))
print('В комнате room_2 живут: ' + ", ".join(map(str, folks_2)))
