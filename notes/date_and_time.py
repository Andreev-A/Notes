# now_date = datetime.date.today()  # Текущая дата (без времени)
# now_time = datetime.datetime.now()  # Текущая дата со временем
#
# cur_year = now_date.year  # Год текущий
# cur_month = now_date.month  # Месяц текущий
# cur_day = now_date.day  # День текущий
# cur_hour = now_time.hour  # Час текущий
# cur_minute = now_time.minute  # Минута текущая
# cur_second = now_time.second  # Секунда текущие
# num_week = now_date.isoweekday()  # узнаем день недели (от 1 до 7)
#
# now_date = now_date.replace(2011, 6, 30)  # меняем полностью дату на 30.06.2011
# now_date = now_date.replace(day=cur_day)  # меняем только день
# now_date = now_date.replace(month=cur_month)  # меняем только месяц
# now_date = now_date.replace(year=cur_year)  # меняем только год
#
# ny_2011 = datetime.date(2011, 2, 1)  # создали дату: 1 февраля 2011 года
# delta = ny_2011 - now_date  # разница (дельта) в между 2-мя датами
#
# delta = datetime.timedelta(days=2)  # дельта в 2 дня
# now_date = now_date + delta  # Узнаем какое число будет через 2 дня
# now_date = now_date - delta  # или какое число было 2 дня назад
# num_week = now_date.isoweekday() # узнаем номер недели (от 1 до 7)
#
# y, m, d = map(int, input().split())
# date = datetime.datetime.strptime(input(), "%Y %m %d")
# ymd = datetime.date(*[int(i) for i in input().split()])
# dd = datetime.date(*map(int, input().split()))
#
# print(now_time.strftime("%d.%m.%Y %I:%M %p"))  # форматируем дату
# print(a.year, a.month, a.day)  # возвращают аргументы в формате int
# print("{} {} {}".format(year, month, day))
# print(f'{inp.year} {inp.month} {inp.day}')
# На винде пишем так:  datetime.datetime.strftime(Дата в формате datetime , '%Y %#m %#d' )
# На линукс пишем так:  datetime.datetime.strftime(Дата в формате datetime , '%Y %-m %-d' )
#
# %S — секунды. От 0 до 61
# %M — минуты. От 00 до 59
# %H — час. От 00 до 23
# %I — час. От 1 до 12
# %p -После перед полуднем или после (AM или PM)
# %d — день. От 01 до 31
# %j — день как номер года. От 001 до 366
# %m — месяц. От 01 до 12
# %y — год в виде 2-х последних чисел. От 00 до 99
# %Y — год в виде полного числа

########################################################################################################################
# В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
# Во второй строке дано одно число days -- число дней.
# Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней,
# равное days.

# import datetime
#
# date = datetime.datetime.strptime(input(), "%Y %m %d")
# date += datetime.timedelta(days=int(input()))
# print(datetime.datetime.strftime(date, '%Y %#m %#d'))
# print(date.year, date.month, date.day)
# print(date.strftime('%Y %#m %#d'))
#
#
# y, m, d = map(int, input().split())
# days = int(input())
# current = datetime.date(year=y, month=m, day=d)
# current += datetime.timedelta(days=days)
# print("{} {} {}".format(current.year, current.month, current.day))
