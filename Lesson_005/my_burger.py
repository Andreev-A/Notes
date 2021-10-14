def add_buns(_recipe):
    need_to_add = input('Добавить в бургер булочки? (да, нет): ').lower()
    if need_to_add == 'да':
        return _recipe.append('булочки')


def add_cutlets(_recipe):
    need_to_add = input('Добавить в бургер котлеты? (да, нет): ').lower()
    if need_to_add == 'да':
        return _recipe.append('котлеты')


def add_cucumber(_recipe):
    need_to_add = input('Добавить в бургер огурчик? (да, нет): ').lower()
    if need_to_add == 'да':
        return _recipe.append('огурчик')


def add_tomato(_recipe):
    need_to_add = input('Добавить в бургер помидор? (да, нет): ').lower()
    if need_to_add == 'да':
        return _recipe.append('помидор')


def add_sauce(_recipe):
    need_to_add = input('Добавить в бургер соус? (да, нет): ').lower()
    if need_to_add == 'да':
        return _recipe.append('соус')


def add_mayonnaise(_recipe):
    need_to_add = input('Добавить в бургер майонеза? (да, нет): ').lower()
    if need_to_add == 'да':
        return _recipe.append('майонез')


def add_cheese(_recipe):
    need_to_add = input('Добавить в бургер сыра? (да, нет): ').lower()
    if need_to_add == 'да':
        return _recipe.append('сыр')
