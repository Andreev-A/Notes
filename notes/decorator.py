# def shout(word="да"):
#     return word.capitalize() + "!"
#
#
# print(shout())
# # выведет: 'Да!'
#
# # Так как функция - это объект, её можно связать с переменнной, как и любой другой объект
# scream = shout
#
# # Заметьте, что мы не используем скобок: мы НЕ вызываем функцию "shout", # мы связываем её с переменной "scream".
# # Это означает, что теперь мы можем вызывать "shout" через "scream":
#
# print(scream())
# # выведет: 'Да!'
#
# # Более того, это значит, что мы можем удалить "shout", и функция всё ещё будет доступна через переменную "scream"
#
# del shout
# try:
#     print(shout())
# except NameError as e:
#     print(e)
#     # выведет: "name 'shout' is not defined"
#
# print(scream())
# # выведет: 'Да!'
#
# def talk():
#     # Внутри определения функции "talk" мы можем определить другую...
#     def whisper(word="да"):
#         return word.lower() + "..."
#     # ... и сразу же её использовать!
#     print(whisper())
#
# # Теперь, КАЖДЫЙ РАЗ при вызове "talk", внутри неё определяется а затем и вызывается функция "whisper".
# talk()
# # выведет: "да..."
# # Но вне функции "talk" НЕ существует никакой функции "whisper":
# try:
#     print(whisper())
# except NameError as e:
#     print(e)
#     # выведет: "name 'whisper' is not defined"