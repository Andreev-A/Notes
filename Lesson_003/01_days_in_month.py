# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
# user_input = input("Введите, пожалуйста, номер месяца: ")
# month = int(user_input)
# days_number = 0

# TODO здесь ваш код
user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
days_number = 0
if month in (1, 3, 5, 7, 8, 10, 12):
    days_number = 31
elif month in (4, 6, 9, 11):
    days_number = 30
elif month == 2:
    days_number = 28
else:
    print('Некорректный номер месяца')

if 0 < month <= 12:
    print('Количество дней в месяце -', days_number)
