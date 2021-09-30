# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

# educational_grant, expenses = 10000, 12000

# TODO здесь ваш код
educational_grant, expenses = 10000, 12000
month = 10
total_educational_grant = educational_grant
expenses_next = expenses
while total_educational_grant < educational_grant * month:
    expenses_next = expenses_next * 1.03
    expenses += expenses_next
    total_educational_grant += educational_grant
take_from_parents = round(expenses - total_educational_grant, 2)
print('Студенту надо попросить', take_from_parents, 'рублей')
