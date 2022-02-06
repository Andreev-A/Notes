# Регулярные выражения в Python
# Оригинальная документация на английском:
# https://docs.python.org/3/library/re.html
# Очень подробный и обстоятельный материал на английском:
# https://www.regular-expressions.info/
# Удобный сервис для тестирования и отладки регулярных выражений (не забудьте выбрать Python):
# https://regex101.com/
# Онлайн визуализация регулярок (не забудьте выбрать Python):
# https://www.debuggex.com/
# Лист с подсказками синтаксиса сгруппированный и компактный:
# https://www.debuggex.com/cheatsheet/regex/python
# Статья -  https://tproger.ru/translations/regular-expression-python
# Шпаргалка - http://www.exlab.net/files/tools/sheets/regexp/regexp.pdf
# http://pythex.org/ - весьма удобный инструмент, позволяющий "в живую" смотреть на то, как работают reg exp.
# Хорошая статья по регуляркам в python - https://habrahabr.ru/post/349860/

# Для того, чтобы указать, что строка является сырой (raw), перед ней нужно добавить символ r
# x = 'Hello\nword'
# print(x)
# x = r'Hello\nword'  # raw
# print(x)
# Сырые строки используют тогда, когда нужно в записи строки использовать обратный слеш. В частности, в регулярных
# выражениях.
# Для использования регулярных выражений подключаем модуль re (regular expressions):
# import re
# print(re.match)
# print(re.search)
# print(re.findall)
# print(re.sub)

# Функция match
# Ищет совпадение по заданному шаблону в начале строки.
# pattern = r"abc"
# string = "abcd"
# match_object = re.match(pattern, string)
# print(match_object)  # <re.Match object; span=(0, 3), match='abc'>
# [] можно указывать множество подходящих символов (любой из указанных)
# pattern = r"a[abc]c"
# string = "accd"

# Функция search
# Находит в строке первую подстроку, которая подходит под заданный шаблон.
# pattern = r"abc"
# string = "babcd"
# match_object = re.search(pattern, string)
# print(match_object)  # <re.Match object; span=(1, 4), match='abc'>

# Функция findall
# Находит в строке все подстроки, которые подходят под заданный шаблон. Возвращает все непересекающиеся подстроки.
# Для того, чтобы группа не попадала в список возвращаемый findall, есть специальный синтаксис (?:выражение).
# pattern = r"a[abc]c"
# string = "abc, a.c, aac, a-c, aBc, azc, aaa"
# all_inclusions = re.findall(pattern, string)
# print(all_inclusions)  # ['abc', 'aac']

# Функция sub
# Позволит заменить все подстроки, которые подходят под заданный шаблон, чем-нибудь другим.
# pattern = r"a[abc]c"
# string = "abc, a.c, aac, a-c, aBc, azc, aaa"
# fixed_typos = re.sub(pattern, "abc", string)
# print(fixed_typos)  # abc, a.c, abc, a-c, aBc, azc, aaa

# Собственно, регулярные выражения и будут описывать шаблон.

# match сравнивает - подходит ли вся строка под наш шаблон, а search - просто ищет вхождение шаблона в строку.
# Т.е., если грубо, то в шаблоне может быть забит пример регулярки для email вида foo@bar.tld. И match проверяет -
# действительно ли в строке электропочта (email@gmail.com), а search может найти подходящий под шаблон кусок строки,
# хотя сама строка не является валидным адресом (em@am@email@gmail.com111).

# Можно из dir(match_object) вытащить, чего в нем есть:
# import re
# mo = re.search(r"a[xyz]c", "abc_axc_azc")
# print(dir(mo))  # [ ...все атрибуты...]
# print(mo)       # <re.Match object; span=(4, 7), match='axc'>
# print(mo.string, mo.pos, mo.endpos)     # abc_axc_azc 0 11
# print(mo.group(), mo[0])                # axc axc
# print(mo.span(), mo.start(), mo.end())  # (4, 7) 4 7

# Пример использования регулярных выражений:
# pattern = r"a.c"
# string = "acc"
# match_object = re.match(pattern, string)
# print(match_object)  # <re.Match object; span=(0, 3), match='acc'>
#
# string = "abc, a.c, aac, a-c, aBc, azc, aaa"
# all_inclusions = re.findall(pattern, string)
# print(all_inclusions)  # ['abc', 'a.c', 'aac', 'a-c', 'aBc', 'azc']
#
# fixed_typos = re.sub(pattern, "abc", string)
# print(fixed_typos)  # abc, abc, abc, abc, abc, abc, aaa

# Метосимвол обозначает, что нам надо сделать что-то специальное. Если надо использовать метасимвол в качестве обычного
# символа его надо экранировать обратным слешем - \?.
# [] -- можно указать множество подходящих символов
# [abc] - указанные символы
# [a-zA-Z] - указанный диапазон (в примере все символы алфавита)
# [^a-zA-Z] - символ карет(циркум флекс) ^ позволяет задать множество символов, которые не подходят
# ^ - карет, обозначает либо начало строки, либо инвертирование группы символов. (например: "^[^0-9]" — не цифра в
# начале строки).
# . ^ $ * + ? { } [ ] \ | ( ) -- метасимволы
# короткая запись часто используемых выражений:
# \d ~ [0-9] -- цифры
# \D ~ [^0-9]
# \s ~ [ \t\n_test\r\input_file\v] -- пробельные символы
# \S ~ [^ \t\n_test\r\input_file\v]
# \w ~ [a-zA-Z0-9_] -- буквы + цифры + _
# \W ~ [^a-zA-Z0-9_]
# пример - r"a[\w.]c" - буквы + цифры + _ и точка (дополнить короткую запись)
# пример - r"a.c" - любой символ, кроме переноса строки
# пример - r"ab*c" - любое число повторений заданного символа, включая его отсутствие
# пример - r"ab+c" - любое число повторений заданного символа, один и более
# пример - r"ab?c" - означает 0 или 1 вхождение символа
# пример - r"ab{3}c" - задает конкретное количество или диапазон вхождений символа - {2, 5}. В фигурных скобках после
# запятой можно ничего не ставить и искать больше или равно символов чем n_test - {3, }, { , 3}.
# pattern = r"ab{2,4}a"
# string = "aa, aba, abba, abbba, abbbba, abbbbba"
# all_inclusions = re.findall(pattern, string)
# print(all_inclusions)  # ['abba', 'abbba', 'abbbba']

# Метасимволы являются “жадными”. Поэтому по умолчанию, если под шаблон подходят несколько вариантов вхождений, то
# вернется самый длинный из них.
# pattern = r"a[ab]+a"
# string = "abaaba"
# print(re.match(pattern, string))  # <re.Match object; span=(0, 6), match='abaaba'>
# print(re.findall(pattern, string))  # ['abaaba']

# Мы можем указать функции, что хотим искать не жадным способом (ленивым) Т.е. найти наименьшее вхождение, которое бы
# удовлетворило нашему регулярному выражению. Для этого мы можем использовать ? после нашего метасимвола:
# pattern = r"a[ab]+?a"
# string = "abaaba"
# print(re.match(pattern, string))  # <re.Match object; span=(0, 3), match='aba'>
# print(re.findall(pattern, string))  # ['aba', 'aba']

# То есть можем использовать для нахождения повторов символа или группы, но аккуратно - т.к. по умолчанию он "жадный".
# пример - r"(test)*" - группировка нескольких символов
# pattern = r"(test)*"
# string = "testtest"
# print(re.match(pattern, string))  # <re.Match object; span=(0, 8), match='testtest'>
# пример - r"(test|text)*" - операция или к элементам. Обладает наименьшим приоритетом в регулярных выражениях.
# pattern = r"(test|text)*"
# string = "texttest"
# print(re.match(pattern, string))  # <re.Match object; span=(0, 8), match='texttest'>
# Методы группировки
# pattern = r"((abc)|(test|text)*)"
# string = "texttest"
# match = re.match(pattern, string)
# print(match)  # <re.Match object; span=(0, 8), match='texttest'>
# print(match.groups())  # ('texttest', None, 'test') 3 группа последнее вхождение test
# Метод групп с явной передачей номера группы
# pattern = r"Hello (abc|text)"
# string = "Hello abc"
# match = re.match(pattern, string)
# print(match)  # <re.Match object; span=(0, 9), match='Hello abc'>
# print(match.group())  # Hello abc
# print(match.group(1))  # abc

# Использование группы внутри регулярного выражения
# pattern = r"(\w+)-\1"  # \1 - говорит - найди такую же группу, как ты собрал ранее (номер группы по открывающей скобке)
# string = "test-test"  # не допустим "test-text" потому что не совпадает с первой группой
# match = re.match(pattern, string)
# print(match)  # <re.Match object; span=(0, 9), match='test-test'>

# Оставить только первую группу из повторяющихся
# pattern = r"(\w+)-\1"
# string = "test-test chow-chow"
# duplicates = re.sub(pattern, r'\1', string)
# print(duplicates)  # test chow

# Аккуратно с группами с findall - будет возвращать кортеж групп
# Для того, чтобы группа не попадала в список возвращаемый findall, есть специальный синтаксис (?:выражение).
# pattern = r"(\w+)-\1"
# string = "test-test chow-chow"
# duplicates = re.findall(pattern, string)
# print(duplicates)  # ['test', 'chow']
#
# pattern = r"((\w+)-\2)"  # кортеж - первое поймали сначала группу, а второй наше слово, которое через дефис удвоили
# string = "test-test chow-chow"
# duplicates = re.findall(pattern, string)
# print(duplicates)  # [('test-test', 'test'), ('chow-chow', 'chow')]

# Если нам нужно найти " english\?"
# ? тогда - "  english\\\?"
# символ карет удобно и быстро вводить альт-кодом 94, зажимаете alt и набираете 94
# \r перенос каретки как бы все подтирает, что было в строке до нее, начиная строку с начала (добавляя еще белое
# пространство).
# Дефис внутри квадратных скобок будет считаться как обычный символ только в двух случаях:
# дефис экранирован слэшем [a\-c] - это значит, что допускается один из трех символов a, с, -
# дефис идет в начале или в конце выражения: [-ac] или [ac-]
# Во всех остальных случаях дефис будет идти как идентификартор рейнджа. Так как рейнджа w-. не существует, то
# интерпретатор выдает ошибку. А вот на [\w.-] не ругается.

# А почему если :
# pattern = r'(test)*'
# string = 'testtest'
# то,
# print(re.findall(pattern, string))  # ['test', ''] ????
# почему не
# ['test', 'test'] ??
# Если в паттерне присутствует одна или более групп, то возвращается список групп. А пустая строка вторым элементом в
# выдаче потому, что *, а её устраивает 0. Если pattern = r'(test)+', то пустой строки не будет.


# Зачем использовать сырые строки, если модуль re все равно воспринимает их как "несырые", т.е. экранирование не
# отключается?
# Все правильно. Потому, что для \? нет escape-последовательности. Попробуем по другому:
# Дана строка
# str_01 = 'one\\t'
# print(str_01)  # one\t
# Два шаблона
# pat_01 = 'one\\t'
# pat_02 = r'one\\t'
# print(re.match(pat_01, str_01))  # None
# print(re.match(pat_02, str_01))  # < re.Match object; span = (0, 5), match = 'one\\t' >
# В первом случаем мы искали Табуляцию (\t), (после экранирующего слеша получилось \t, в регулярном выражение - это
# значит искать табуляцию). Во втором случае искали \\t (то есть \t  в "голом" тексте).
# Рекомендуют сразу применять "сырые" строки, чтобы таких накладок не было. Применил, и думать забыл.
# Escape-последовательности, это такой набор символов, с помощью которого можно вывести на экран невидимые, или
# управляющие символы. Например:
# перевод строки (\n_test):
# print("Hello\nHello")
# Hello
# Hello
# Или горизонтальная табуляция (\t) - аналогична клавише Tab:
# print("Hello\tHello")
# Hello    Hello
# Или клавиша backspace (удалить последний символ) - \b:
# print("Hello\b")
# Hell
# Сырые строки работаю везде, не только в модуле re.
# Например:
# print(r"Hello\tHello")
# Hello\tHello
# Обратите внимание, что в строке не сработала последовательность- \t . Табуляции уже нет. То есть строка отобразилась
# на экране, как есть. То есть "сырая", без обработки.
# А вообще, совет такой. Возьмите себе за привычку, везде применять обычные строки. В шаблонах модуля re, применять
# сырые строки.
# И для примера. Вам вдруг понадобилось вывести такую строку на экран "Тут будет перевод строки\nА это новая строка".
# То лучшем решением будет сделать так:
# print("Тут будет перевод строки\\nА это новая строка") - то есть добавить экранирующий слэш (\)
# А вот если шаблон для регулярного выражения, то сразу без раздумий пишите:
# pattern = r"*.A{2}"
# Так принято в народе. Да и вы перестанете думать, где надо сырая, а где нет. Как и я.

# Нашла опытным путем, что [а-яё] можно заменить на [а-ё], а вот с [A-Ё] так не получится. Потому что судя по всем
# алфавит идет так эюяё ЁАБВ. Поэтому заглавные пишем так: [Ё-Я]. Итого, ваш код можно переписать так:
# import re
# regex1 = r"\b[а-яА-Я]+"
# regex2 = r"\b[а-ёЁ-Я]+"
# s = "Ежиха ела ёлку. Ёжик сел на ель."
# print(re.findall(regex1, s))
# print(re.findall(regex2, s))

# def print_chr(start=1000, end=1111):
#     print('      ', end='')
#     for i in range(10):
#         print(i, end=' ')
# for i in range(1000, 1111):
#     if i % 10 == 0:
#         print('\n_test', i, end=' ')
#     print(chr(i), end=' ')
# print()
# print_chr()
# 0 1 2 3 4 5 6 7 8 9
#  1000 Ϩ ϩ Ϫ ϫ Ϭ ϭ Ϯ ϯ ϰ ϱ
#  1010 ϲ ϳ ϴ ϵ ϶ Ϸ ϸ Ϲ Ϻ ϻ
#  1020 ϼ Ͻ Ͼ Ͽ Ѐ Ё Ђ Ѓ Є Ѕ
#  1030 І Ї Ј Љ Њ Ћ Ќ Ѝ Ў Џ
#  1040 А Б В Г Д Е Ж З И Й
#  1050 К Л М Н О П Р С Т У
#  1060 Ф Х Ц Ч Ш Щ Ъ Ы Ь Э
#  1070 Ю Я а б в г д е ж з
#  1080 и й к л м н о п р с
#  1090 т у ф х ц ч ш щ ъ ы
#  1100 ь э ю я ѐ ё ђ ѓ є ѕ
#  1110 і

# Регулярное выражение — это строка, задающая шаблон поиска подстрок в тексте. Одному шаблону может соответствовать
# много разных строчек.
# Регулярное выражение, или коротко «регулярка», состоит из обычных символов и специальных командных
# последовательностей. Например, \d задаёт любую цифру, а \d+ — задает любую последовательность из одной или более цифр.
# import re
#
# x = re.match(r"(te)*?xt", "TEXT", re.IGNORECASE | re.DEBUG)
# print(x)

# При использовании re.sub так флаг работать не будет:
# print(re.sub(r'(te)*?xt', 'color', 'TEXT', re.IGNORECASE))
# документация говорит, что будет работать только при явном использовании именованного аргумента:
# print(re.sub(r'(te)*?xt', 'color', 'TEXT', flags=re.IGNORECASE))

# Использование такой конструкции, как "cat.*cat". То есть мы ищем строки, в которых есть хотя бы два слова cat, между
# которыми может быть любое количество любых символов

# Если мы указываем строку '\\', то в итоге у нас получится строка '\', при обработке (первый символ экранирования,
# второй уже непосредственно символ). Нам же надо, чтобы в модуль re ушла строка '\\'. Т.е. если не использовать raw,
# то надо передовать в модуль строку '\\\\'. В этом случае при работе программы модуль получит строку '\\', и один из
# символов \ будет считаться служебным.

# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
# import sys
# import re
# for line in sys.stdin:
#     line = line.rstrip()
#     if len(re.findall(r"cat", line)) > 1:
#         print(line)
#
# for line in sys.stdin:  # пример правильного решения и регулярного выражения
#     line = line.strip()
#     if re.search(r"cat.*cat", line):
#         print(line)
#
# pattern = r"(.*(cat).*){2,}"
# [print(line.rstrip()) for line in sys.stdin if re.match(pattern, line)]

# Вам дана последовательность строк.
# Выведите строки, содержащие "cat" в качестве слова.
# import sys
# import re
# for line in sys.stdin:
#     line = line.strip()
#     if re.search(r"\bcat\b", line):
#         print(line)

# Вам дана последовательность строк.
# Выведите строки, содержащие две буквы "z", между которыми ровно три символа.
# import sys
# import re
# for line in sys.stdin:
#     line = line.strip()
#     if re.search(r"z...z", line):  # if re.search(r'z.{3}z', line):
#         print(line)

# Вам дана последовательность строк.
# Выведите строки, содержащие обратный слеш "\".
# import sys
# import re
# for line in sys.stdin:
#     line = line.strip()
#     if re.search(r"\\", line):  # input_file chr(92) in line:
#         print(line)

# Вам дана последовательность строк.
# Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).
# import sys
# import re
# for line in sys.stdin:
#     line = line.strip()
#     if re.search(r"\b(\w+)\1\b", line):  # (r"(\b.*\B)\1\b", line)  if re.match(r'\b(.+)\1\b', line):
#         print(line)
# '\B' обозначает, что после предыдущего символа нет пробела. В варианте r"(\b.*\B)\1\b" представьте, что мы  сначала
# ищем блок (пробел + любое количество любых символов кроме пробела + не пробел), а потом проверяем есть ли рядом с ним
# такая же последовательность символов и пробел.

# Вам дана последовательность строк.
# В каждой строке замените все вхождения подстроки "human" на подстроку "computer" и выведите полученные строки.
# import sys
# import re
# for line in sys.stdin:
#     line = line.strip()
#     print(re.sub(r"human", "computer", line))  #
#
# print(re.sub(r'human', 'computer', sys.stdin.read()), end='')

# Вам дана последовательность строк.
# В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" (регистр не важен), на
# слово "argh".
# import sys
# import re
# for line in sys.stdin:
#     line = line.strip()
#     print(re.sub(r"\b[aA]+\b", "argh", line, 1))  #
#
# for line in sys.stdin:  # Пример правильного использования аргумента count и использования флага re.IGNORCASE
#     line = line.strip()
#     line = re.sub(r"\ba+\b", "argh", line, count=1, flags=re.IGNORECASE)
#     print(line)
#
# [print(re.sub(r'\b[aA]+\b', 'argh', line.rstrip(), 1)) for line in sys.stdin]

# Вам дана последовательность строк.
# В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
# Буквой считается символ из группы \w.
# import sys
# import re
# # for line in sys.stdin:
# #     line = line.strip()
# #     print(re.sub(r"\b(\w)(\w)(\b|\B)", r"\2\1", line))  #
#
# for line in sys.stdin:  # пример правильного решения
#     line = line.strip()
#     line = re.sub(r"\b(\w)(\w)(\w*)\b", r"\2\1\3", line)
#     print(line)
#
# for line in sys.stdin:
#     line = line.rstrip()
#     print(re.sub(r'\b(\w)(\w)', r"\2\1", line))

# Вам дана последовательность строк.
# В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
# Буквой считается символ из группы \w.
# import sys
# import re
# for line in sys.stdin:
#     line = line.strip()
#     print(re.sub(r"(\w)\1+", r"\1", line))  #

# Существенной проблемой, однако, является то, что в простейшем варианте регэкспы работают только для латиницы.
# Использование их с кириллицей требует определённых дополнительных усилий.
# Собственно, дело в том, что все строки в Питоне хранятся в формате str, который всегда имеет определённую кодировку
# (utf8, cp1251, koi8r и т. д.), а сам Питон работает с текстом в формате unicode. Для латиницы это обычно проблем не
# вызывает, а вот для кириллицы разница существенная.
# Рецепт борьбы прост. Надо проводить все действия в формате unicode. Для того, чтобы задать строку в юникоде,
# необходимо перед ней добавить букву u:
# > text = u'Текст'
# Если у вас уже есть некий текст в известной кодировке (например, вы прочли его из файла или скачали из интернета), то
# его следует перекодировать в юникод с помощью команд unicode или decode:
# > unicode_text = unicode(utf8_text, 'utf8')
# > unicode_text = utf8_text.decode('utf8')
# Далее необходимо при использовании регулярных выражений не забывать и их переводить в юникод:
# > regexp = re.compile(u'[а-я]')
# Проверьте, теперь команда
# > re.sub(regexp, '', 'КрасОТИЩЕ')
# должна выдавать
# > КОТИЩЕ


# input = '10010'
# res = 0
# if input.isdigit():
#     for i, val in enumerate(input):
#         if i % 2:
#             res += int(val)
#         else:
#             res -= int(val)
# if not (res) % 3:
#     print('yes')

# Используя некоторые базовые правила регулярных выражений, это упрощает
# (1(01*0)*1|0)*


# import sys
# import re
#
# for line in sys.stdin:
#     line = line.strip()
#     if re.search(r"\A[01]+\Z",line):
#          if re.fullmatch(r"REG-EXP",line[::-1]):
#              print(line)

import requests

res = requests.get("https://www.google.com/search/",
                   params={"q": "Stepik"})
print(res.status_code)
print(res.headers['Content-Type'])
print(res.url)
print(res.text)


# Основы регулярных выражений
# Регулярками называются шаблоны, которые используются для поиска соответствующего фрагмента текста и сопоставления
# символов.
# Грубо говоря, у нас есть input-поле, в которое должен вводиться email-адрес. Но пока мы не зададим проверку валидности
# введённого email-адреса, в этой строке может оказаться совершенно любой набор символов, а нам это не нужно.
# Чтобы выявить ошибку при вводе некорректного адреса электронной почты, можно использовать следующее рег. выражение:
# r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$'
# По сути, наш шаблон — это набор символов, который проверяет строку на соответствие заданному правилу.
# Давайте разберёмся, как это работает.
# Синтаксис RegEx
# Синтаксис у регулярок необычный. Символы могут быть как буквами или цифрами, так и метасимволами, которые задают
# шаблон строки:



# Также есть дополнительные конструкции, которые позволяют сокращать регулярные выражения:
# \d — соответствует любой одной цифре и заменяет собой выражение [0-9];
# \D — исключает все цифры и заменяет [^0-9];
# \w — заменяет любую цифру, букву, а также знак нижнего подчёркивания;
# \W — любой символ кроме латиницы, цифр или нижнего подчёркивания;
# \s — соответствует любому пробельному символу;
# \S — описывает любой непробельный символ.
# Для чего используются регулярные выражения
# для определения нужного формата, например телефонного номера или email-адреса;
# для разбивки строк на подстроки;
# для поиска, замены и извлечения символов;
# для быстрого выполнения нетривиальных операций.
# Синтаксис  таких выражений в основном стандартизирован, так что вам следует понять их лишь раз, чтобы использовать в
# любом языке программирования.
# Примечание Не стоит забывать, что регулярные выражения не всегда оптимальны, и для простых операций часто достаточно
# встроенных в Python функций.

# Регулярные выражения в Python
# В Python для работы с регулярками есть модуль re. Его нужно просто импортировать:
# import re
# А вот наиболее популярные методы, которые предоставляет модуль:
# re.match()
# re.search()
# re.findall()
# re.split()
# re.sub()
# re.compile()
# Рассмотрим каждый из них подробнее.

# re.match(pattern, string)
# Этот метод ищет по заданному шаблону в начале строки. Например, если мы вызовем метод match() на строке «AV Analytics
# AV» с шаблоном «AV», то он завершится успешно. Но если мы будем искать «Analytics», то результат будет отрицательный:
#
# import re
# result_dict = re.match(r'AV', 'AV Analytics Vidhya AV')
# print result_dict
#
# Результат:
# <_sre.SRE_Match object at 0x0000000009BE4370>
# Искомая подстрока найдена. Чтобы вывести её содержимое, применим метод group() (мы используем «r» перед строкой
# шаблона, чтобы показать, что это «сырая» строка в Python):
#
# result_dict = re.match(r'AV', 'AV Analytics Vidhya AV')
# print result_dict.group(0)
#
# Результат:
# AV
# Теперь попробуем найти «Analytics» в данной строке. Поскольку строка начинается на «AV», метод вернет None:
#
# result_dict = re.match(r'Analytics', 'AV Analytics Vidhya AV')
# print result_dict
#
# Результат:
# None
# Также есть методы start() и end() для того, чтобы узнать начальную и конечную позицию найденной строки.
#
# result_dict = re.match(r'AV', 'AV Analytics Vidhya AV')
# print result_dict.start()
# print result_dict.end()
#
# Результат:
# 0
# 2
# Эти методы иногда очень полезны для работы со строками.

# re.search(pattern, string)
# Метод похож на match(), но ищет не только в начале строки. В отличие от предыдущего, search() вернёт объект, если мы
# попытаемся найти «Analytics»:
#
# result_dict = re.search(r'Analytics', 'AV Analytics Vidhya AV')
# print result_dict.group(0)
#
# Результат:
# Analytics
# Метод search() ищет по всей строке, но возвращает только первое найденное совпадение.
#
# re.findall(pattern, string)
# Возвращает список всех найденных совпадений. У метода findall() нет ограничений на поиск в начале или конце строки.
# Если мы будем искать «AV» в нашей строке, он вернет все вхождения «AV». Для поиска рекомендуется использовать именно
# findall(), так как он может работать и как re.search(), и как re.match().
#
# result_dict = re.findall(r'AV', 'AV Analytics Vidhya AV')
# print result_dict
#
# Результат:
# ['AV', 'AV']
# re.split(pattern, string, [maxsplit=0])
# Этот метод разделяет строку по заданному шаблону.
#
# result_dict = re.split(r'y', 'Analytics')
# print result_dict
#
# Результат:
# ['Anal', 'tics']
# В примере мы разделили слово «Analytics» по букве «y». Метод split() принимает также аргумент maxsplit со значением по
# умолчанию, равным 0. В данном случае он разделит строку столько раз, сколько возможно, но если указать этот аргумент,
# то разделение будет произведено не более указанного количества раз. Давайте посмотрим на примеры Python RegEx:
#
# result_dict = re.split(r'i', 'Analytics Vidhya')
# print result_dict
#
# Результат:
# ['Analyt', 'cs V', 'dhya'] # все возможные участки.
# result_dict = re.split(r'i', 'Analytics Vidhya',maxsplit=1)
# print result_dict
#
# Результат:
# ['Analyt', 'cs Vidhya']
# Мы установили параметр maxsplit равным 1, и в результате строка была разделена на две части вместо трех.
#
# re.sub(pattern, repl, string)
# Ищет шаблон в строке и заменяет его на указанную подстроку. Если шаблон не найден, строка остается неизменной.
#
# result_dict = re.sub(r'India', 'the World', 'AV is largest Analytics community of India')
# print result_dict
#
# Результат:
# 'AV is largest Analytics community of the World'
# re.compile(pattern, repl, string)
# Мы можем собрать регулярное выражение в отдельный объект, который может быть использован для поиска. Это также
# избавляет от переписывания одного и того же выражения.
#
# pattern = re.compile('AV')
# result_dict = pattern.findall('AV Analytics Vidhya AV')
# print result_dict
# result2 = pattern.findall('AV is largest analytics community of India')
# print result2
#
# Результат:
# ['AV', 'AV']
# ['AV']
# До сих пор мы рассматривали поиск определенной последовательности символов. Но что, если у нас нет определенного
# шаблона, и нам надо вернуть набор символов из строки, отвечающий определенным правилам? Такая задача часто стоит при
# извлечении информации из строк. Это можно сделать, написав выражение с использованием специальных символов. Вот
# наиболее часто используемые из них:

# Оператор	Описание
# .	Один любой символ, кроме новой строки \n_test.
# ?	0 или 1 вхождение шаблона слева
# +	1 и более вхождений шаблона слева
# *	0 и более вхождений шаблона слева
# \w	Любая цифра или буква (\W — все, кроме буквы или цифры)
# \d	Любая цифра [0-9] (\D — все, кроме цифры)
# \s	Любой пробельный символ (\S — любой непробельный символ)
# \b	Граница слова
# [..]	Один из символов в скобках ([^..] — любой символ, кроме тех, что в скобках)
# \	Экранирование специальных символов (\. означает точку или \+ — знак «плюс»)
# ^ и $	Начало и конец строки соответственно
# {n_test,m}	От n_test до m вхождений ({,m} — от 0 до m)
# a|b	Соответствует a или b
# ()	Группирует выражение и возвращает найденный текст
# \t, \n_test, \r	Символ табуляции, новой строки и возврата каретки соответственно
# Больше информации по специальным символам можно найти в документации для регулярных выражений в Python 3.
#
# Перейдём к практическому применению Python регулярных выражений и рассмотрим примеры.
#
# Задачи
# Вернуть первое слово из строки
# Сначала попробуем вытащить каждый символ (используя .)
#
# result_dict = re.findall(r'.', 'AV is largest Analytics community of India')
# print result_dict
#
# Результат:
# ['A', 'V', ' ', 'i', 's', ' ', 'l', 'a', 'r', 'g', 'e', 's', 't', ' ', 'A', 'n_test', 'a', 'l', 'y', 't', 'i', 'c', 's',
# ' ', 'c', 'o', 'm', 'm', 'u', 'n_test', 'i', 't', 'y', ' ', 'o', 'input_file', ' ', 'I', 'n_test', 'd', 'i', 'a']
# Для того, чтобы в конечный результат не попал пробел, используем вместо . \w.

# result_dict = re.findall(r'\w', 'AV is largest Analytics community of India')
# print result_dict
#
# Результат:
# ['A', 'V', 'i', 's', 'l', 'a', 'r', 'g', 'e', 's', 't', 'A', 'n_test', 'a', 'l', 'y', 't', 'i', 'c', 's', 'c', 'o', 'm',
# 'm', 'u', 'n_test', 'i', 't', 'y', 'o', 'input_file', 'I', 'n_test', 'd', 'i', 'a']
# Теперь попробуем достать каждое слово (используя * или +)
#
# result_dict = re.findall(r'\w*', 'AV is largest Analytics community of India')
# print result_dict
#
# Результат:
# ['AV', '', 'is', '', 'largest', '', 'Analytics', '', 'community', '', 'of', '', 'India', '']
# И снова в результат попали пробелы, так как * означает «ноль или более символов». Чтобы их убрать, используем +:
#
# result_dict = re.findall(r'\w+', 'AV is largest Analytics community of India')
# print result_dict
# Результат:
# ['AV', 'is', 'largest', 'Analytics', 'community', 'of', 'India']
# Теперь вытащим первое слово, используя ^:
#
# result_dict = re.findall(r'^\w+', 'AV is largest Analytics community of India')
# print result_dict
#
# Результат:
# ['AV']
# Если мы используем $ вместо ^, то мы получим последнее слово, а не первое:
#
# result_dict = re.findall(r'\w+$', 'AV is largest Analytics community of India')
# print result_dict
#
# Результат:
# [‘India’]
# Вернуть первые два символа каждого слова
# Вариант 1: используя \w, вытащить два последовательных символа, кроме пробельных, из каждого слова:
#
# result_dict = re.findall(r'\w\w', 'AV is largest Analytics community of India')
# print result_dict
#
# Результат:
# ['AV', 'is', 'la', 'rg', 'es', 'An', 'al', 'yt', 'ic', 'co', 'mm', 'un', 'it', 'of', 'In', 'di']
# Вариант 2: вытащить два последовательных символа, используя символ границы слова (\b):
#
# result_dict = re.findall(r'\b\w.', 'AV is largest Analytics community of India')
# print result_dict
#
# Результат:
# ['AV', 'is', 'la', 'An', 'co', 'of', 'In']
# Вернуть домены из списка email-адресов
# Сначала вернём все символы после «@»:
#
# result_dict = re.findall(r'@\w+', 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
# print result_dict
#
# Результат:
# ['@gmail', '@test', '@analyticsvidhya', '@rest']
# Как видим, части «.com», «.in» и т. д. не попали в результат. Изменим наш код:
#
# result_dict = re.findall(r'@\w+.\w+', 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
# print result_dict
#
# Результат:
# ['@gmail.com', '@test.in', '@analyticsvidhya.com', '@rest.biz']
# Второй вариант — вытащить только домен верхнего уровня, используя группировку — ( ):
#
# result_dict = re.findall(r'@\w+.(\w+)', 'abc.test@gmail.com, xyz@test.in, test.first@analyticsvidhya.com, first.test@rest.biz')
# print result_dict
#
# Результат:
# ['com', 'in', 'com', 'biz']
# Извлечь дату из строки
# Используем \d для извлечения цифр.
#
# result_dict = re.findall(r'\d{2}-\d{2}-\d{4}', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
# print result_dict
#
# Результат:
# ['12-05-2007', '11-11-2011', '12-01-2009']
# Для извлечения только года нам опять помогут скобки:
#
# result_dict = re.findall(r'\d{2}-\d{2}-(\d{4})', 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009')
# print result_dict
#
# Результат:
# ['2007', '2011', '2009']
# Задачи по Python для начинающих от Tproger и GeekBrains
# tproger.ru
#
# Извлечь слова, начинающиеся на гласную
# Для начала вернем все слова:
#
# result_dict = re.findall(r'\w+', 'AV is largest Analytics community of India')
# print result_dict
#
# Результат:
# ['AV', 'is', 'largest', 'Analytics', 'community', 'of', 'India']
# А теперь — только те, которые начинаются на определенные буквы (используя []):
#
# result_dict = re.findall(r'[aeiouAEIOU]\w+', 'AV is largest Analytics community of India')
# print result_dict
#
# Результат:
# ['AV', 'is', 'argest', 'Analytics', 'ommunity', 'of', 'India']
# Выше мы видим обрезанные слова «argest» и «ommunity». Для того, чтобы убрать их, используем \b для обозначения
# границы слова:
#
# result_dict = re.findall(r'\b[aeiouAEIOU]\w+', 'AV is largest Analytics community of India')
# print result_dict
#
# Результат:
# ['AV', 'is', 'Analytics', 'of', 'India']
# Также мы можем использовать ^ внутри квадратных скобок для инвертирования группы:
#
# result_dict = re.findall(r'\b[^aeiouAEIOU]\w+', 'AV is largest Analytics community of India')
# print result_dict
#
# Результат:
# [' is', ' largest', ' Analytics', ' community', ' of', ' India']
# В результат попали слова, «начинающиеся» с пробела. Уберем их, включив пробел в диапазон в квадратных скобках:
#
# result_dict = re.findall(r'\b[^aeiouAEIOU ]\w+', 'AV is largest Analytics community of India')
# print result_dict
#
# Результат:
# ['largest', 'community']
# Проверить формат телефонного номера
# Номер должен быть длиной 10 знаков и начинаться с 8 или 9. Есть список телефонных номеров, и нужно проверить их,
# используя регулярки в Python:
#
# li = ['9999999999', '999999-999', '99999x9999']
#
# for val in li:
#     if re.match(r'[8-9]{1}[0-9]{9}', val) and len(val) == 10:
#         print 'yes'
#     else:
#         print 'no'
#
# Результат:
# yes
# no
# no
# Разбить строку по нескольким разделителям
# Возможное решение:
#
# line = 'asdf fjdk;afed,fjek,asdf,foo' # String has multiple delimiters (";",","," ").
# result_dict = re.split(r'[;,\s]', line)
# print result_dict
#
# Результат:
# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
# Также мы можем использовать метод re.sub() для замены всех разделителей пробелами:
#
# line = 'asdf fjdk;afed,fjek,asdf,foo'
# result_dict = re.sub(r'[;,\s]',' ', line)
# print result_dict
#
# Результат:
# asdf fjdk afed fjek asdf foo
# Извлечь информацию из html-файла
# Допустим, нужно извлечь информацию из html-файла, заключенную между <td> и </td>, кроме первого столбца с номером.
# Также будем считать, что html-код содержится в строке.
#
# Пример содержимого html-файла:
#
# 1NoahEmma2LiamOlivia3MasonSophia4JacobIsabella5WilliamAva6EthanMia7MichaelEmily
# С помощью регулярных выражений в Python это можно решить так (если поместить содержимое файла в переменную test_str):
#
# result_dict = re.findall(r'\d([A-Z][A-Za-z]+)([A-Z][A-Za-z]+)', test_str)
# print result_dict
#
# Результат:
# [('Noah', 'Emma'), ('Liam', 'Olivia'), ('Mason', 'Sophia'), ('Jacob', 'Isabella'), ('William', 'Ava'), ('Ethan',
# 'Mia'), ('Michael', 'Emily')]
