import os
from collections import defaultdict
import time

import telebot
import redis

token = '5268671568:AAF9DTbcJZkWcdJVhAHJR0BqhhAakInDhAI'
# token = os.getenv('TOKEN')

bot = telebot.TeleBot(token)

redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379')

# r = redis.Redis(
#     host='localhost',
#     port=6379,
#     db=0,
#     decode_responses=True
# )

r = redis.from_url(redis_url, db=0, decode_responses=True)

START, ADD_NAME, ADD_LOCATION, CONFIRMATION = range(4)

USER_STATE = defaultdict(lambda: START)


def get_state(message):
    return USER_STATE[message.chat.id]


def update_state(message, state):
    USER_STATE[message.chat.id] = state


def write_title_to_redis(message):
    user_id = message.chat.id
    location_title = message.text
    r.lpush(user_id, location_title)


def write_coords_to_redis(user_id, location):
    lat, lon = location.latitude, location.longitude
    title = r.lpop(user_id)
    full_location_data = f'{title}&#124;{lat}&#124;{lon}'
    r.lpush(user_id, full_location_data)


def delete_location(user_id):
    r.lpop(user_id)


@bot.message_handler(
    func=lambda message: get_state(message) == START, commands=['add']
)
def handle_title(message):
    bot.send_message(chat_id=message.chat.id, text='Напишите название места')
    update_state(message, ADD_NAME)


@bot.message_handler(
    func=lambda message: get_state(message) == ADD_NAME)
def handle_location(message):
    if message.text in ('/add', '/list', '/reset'):
        bot.send_message(chat_id=message.chat.id, text='Добавление прервано')
        update_state(message, START)
    else:
        write_title_to_redis(message)
        bot.send_message(chat_id=message.chat.id,
                         text='Отправьте свою геопозицию'
                         )
        update_state(message, ADD_LOCATION)


@bot.message_handler(
    func=lambda message: get_state(message) == ADD_LOCATION,
    content_types=['location']
)
def handle_confirmation(message):
    bot.send_message(chat_id=message.chat.id, text='Добавить место?')
    update_state(message, CONFIRMATION)
    write_coords_to_redis(message.chat.id, message.location)


@bot.message_handler(func=lambda message: get_state(message) == CONFIRMATION)
def handle_finish(message):
    if message.text in ('/add', '/list', '/reset'):
        update_state(message, START)
        delete_location(message.chat.id)
        bot.send_message(chat_id=message.chat.id, text='Добавление прервано')
    else:
        if message.text.lower() in ('да', 'yes', 'ок', 'ok'):
            bot.send_message(
                chat_id=message.chat.id,
                text=f'Место добавлено'
            )
            update_state(message, START)
        elif message.text.lower() in ('нет', 'no'):
            bot.send_message(
                chat_id=message.chat.id,
                text=f'Место не добавлено'
            )
            update_state(message, START)
            delete_location(message.chat.id)
        else:
            bot.send_message(
                chat_id=message.chat.id,
                text=f'Введите да или нет'
            )


@bot.message_handler(
    func=lambda x: True, commands=['list']
)
def handle_list(message):
    if get_state(message) != START:
        update_state(message, START)
        r.lpop(message.chat.id)
    else:
        bot.send_message(chat_id=message.chat.id, text='Последние места:')
        last_locations = r.lrange(message.chat.id, 0, 9)
        for location in last_locations:
            if '&#124;' in location:
                title, lat, lon = location.split('&#124;')
                bot.send_message(chat_id=message.chat.id, text=title)
                bot.send_location(message.chat.id, lat, lon)
            else:
                bot.send_message(chat_id=message.chat.id, text=location)


@bot.message_handler(func=lambda x: True, commands=['reset'])
def handle_confirmation(message):
    r.flushdb()
    bot.send_message(chat_id=message.chat.id, text='Все сохраненные места удалены')


@bot.message_handler(func=lambda x: True, commands=['start'])
def handle_confirmation(message):
    bot.send_message(chat_id=message.chat.id, text='Введите команду /add для добавления места')
    bot.send_message(chat_id=message.chat.id,
                     text='Введите команду /list для просмотра 10 последних мест')
    bot.send_message(chat_id=message.chat.id,
                     text='Введите команду /reset для удаления всех мест')


# bot.polling()
while True:
    try:
        bot.polling(none_stop=True)

    except Exception as e:
        print(e)  # logger.error(e)  # или просто print(e) если у вас логгера нет,
        # или import traceback; traceback.print_exc() для печати полной инфы
        time.sleep(15)


# https://t.me/apower_bot
# 1961796256:AAGeSMjx2sO8hGQq8biD_8ZAInuj3dOe4II    @Apower_TODO_bot
# 5268671568:AAF9DTbcJZkWcdJVhAHJR0BqhhAakInDhAI    t.me/apower_bot.

# Сами разработчики telebot'а предлагают не мудрить и тупо запхнуть polling в вечный цикл и ловить ошибку подключения:
#
# while True:
#     try:
#         bot.polling(none_stop=True)
#
#     except Exception as e:
#         logger.error(e)  # или просто print(e) если у вас логгера нет,
#         # или import traceback; traceback.print_exc() для печати полной инфы
#         time.sleep(15)
# UPD: с многопоточностью (которая по умолчанию) обнаружились проблемы (при перезапуске polling падало в can't start
# thread), можно их обойти, переключившись на однопоточную версию (в простых случаях подойдёт):
#
# bot = telebot.TeleBot(extras.token, threaded=False)

# Есть еще один вариант:
# вместо bot.polling(none_stop=True) написать bot.infinity_polling(True).

# bot.infinity_polling(), True в этом случае лишнее (оно прилетает в timeout=, если его оставить).

####################################################################################################################

# import telebot


# TOKEN = '5268671568:AAF9DTbcJZkWcdJVhAHJR0BqhhAakInDhAI'
#
# bot = telebot.TeleBot(TOKEN, parse_mode=None)  # Вы можете установить parse_mode по умолчанию. HTML или MARKDOWN

# memory
# from collections import defaultdict
#
# START, TITLE, PRICE, CONFIRMATION = range(4)
# USER_STATE = defaultdict(lambda: START)
#
#
# def get_state(message):
#     return USER_STATE[message.chat.id]
#
#
# def update_state(message, state):
#     USER_STATE[message.chat.id] = state
#
# @bot.message_handler(func=lambda message: get_state(message) == START)
# def handle_message(message):
#     bot.send_message(message.chat.id, text='Напишите название')
#     update_state(message, TITLE)
#
#
# @bot.message_handler(func=lambda message: get_state(message) == TITLE)
# def handle_title(message):
#     # название
#     update_product(message.chat.id, 'title', message.text)
#     bot.send_message(message.chat.id, text='Укажи цену')
#     update_state(message, PRICE)
#
#
# @bot.message_handler(func=lambda message: get_state(message) == PRICE)
# def handle_price(message):
#     update_product(message.chat.id, 'price', message.text)
#     product = get_product(message.chat.id)
#     bot.send_message(message.chat.id, text='Опубликовать объявление? {}'.format(product))
#     update_state(message, CONFIRMATION)
#
#
# @bot.message_handler(func=lambda message: get_state(message) == CONFIRMATION)
# def handle_confirmation(message):
#     if 'да' in message.text.lower():
#         bot.send_message(message.chat.id, text='Объявление опубликовано')
#     update_state(message, START)
#
#
# PRODUCTS = defaultdict(lambda: {})
#
# def update_product(user_id, key, value):
#     PRODUCTS[user_id][key] = value
#
# def get_product(user_id):
#     return PRODUCTS[user_id]
#

# # keyboard
# from telebot import types  # для меню
#
# def create_keyboard():
#     keyboard = types.InlineKeyboardMarkup(row_width=2)
#     buttons = [types.InlineKeyboardButton(text=c, callback_data=c) for c in currencies]
#     keyboard.add(*buttons)
#     return keyboard
# @bot.callback_query_handler(func=lambda x: True)
# def callback_handler(callback_query):
#     message = callback_query.message
#     text = callback_query.data
#     currency, value = check_currency_value(text)
#     if currency:
#         bot.answer_callback_query(callback_query.id, text='Курс {} равен {}.'.format(currency, value))  # всплывает
#         # bot.send_message(chat_id=message.chat.id, text='Курс {} равен {}.'.format(currency, value))  # печатается
#     else:
#         bot.send_message(chat_id=message.chat.id, text='Узнай курс валют +')
#
# # message
# currencies = ['евро', 'доллар']
#
# def check_currency(message):
#     for c in currencies:
#         if c in message.text.lower():
#             return True
#     return False
#
#
# def check_currency_value(text):
#     currency_values = {'евро': 70, 'доллар': 60}
#     for currency, value in currency_values.items():
#         if currency in text.lower():
#             return currency, value
#     return None, None
#
#
# @bot.message_handler(commands=['rate'])  # список команд, которые будут обработаны
# @bot.message_handler(func=check_currency)  # фильтр по функции
# def handle_currency(message):
#     print(message.text)
#     currency, value = check_currency_value(message.text)
#     keyboard = create_keyboard()
#     if currency:
#         bot.send_message(chat_id=message.chat.id, text='Курс {} равен {}.'.format(currency, value),
#                          reply_markup=keyboard)
#     else:
#         bot.send_message(chat_id=message.chat.id, text='Узнай курс валют +')
#
# @bot.message_handler()
# def handle_message(message):
#     print(message.text)
#     bot.send_message(message.chat.id, text='Узнай курс валют')
#
#
# # location
# def closest_bank(location):
#     lat = location.latitude
#     lon = location.longitude
#     bank_address = 'Боровичи'
#     bank_lat, bank_lon = 58.687352, 33.958809
#     return bank_address, bank_lat, bank_lon
#
# @bot.message_handler(content_types=['location'])
# def handle_location(message):
#     print(message.location)
#     bank_address, bank_lat, bank_lon = closest_bank(message.location)
#     image = open('sort.png', 'rb')
#     bot.send_photo(message.chat.id, image, caption='Ближайший банк {}'.format(bank_address))
#     # bot.send_message(message.chat.id, text='Ближайший банк {}'.format(bank_address))
#     bot.send_location(message.chat.id, bank_lat, bank_lon)


# bot.polling()


# # -*- coding: utf-8 -*-
# import telebot
#
# token = telebot.TeleBot('1465814143:AAEkiDByuv_ktremloFjYwLxRp7-9jxmucA')
# bot = telebot.TeleBot(token)
#
# @bot.message_handler(commands=['start'])
# def qwe(message):
#   bot.send_message(message.chat.id, 'Привет я бот')
#   bot.send_message(message.chat.id, 'Пока что я раздатчик ролей для игры в мафию!')
#   bot.send_message(message.chat.id, 'Скажи сколько игроков с тобой будет играть (только числами! И от 5 до 10
#   игроков)?')
#
#
# @bot.message_handler(content_types=['text'])
# def igroki(message):
#     if message.text == '11':
#         bot.send_message('Я не могу взять больше 10 игроков !!')
#     else:
#         bot.send_message('Эммм... Я вас не понял!')
#
#
#
# if __name__ == '__main__':
#      bot.polling(none_stop=True)

##################################################################################
#
# from pathlib import Path
#
#
# # Сохраним изображение, которое отправил пользователь в папку `/files/%ID пользователя/photos`
# @bot.message_handler(content_types=['photo'])
# def save_photo(message):
#     # создадим папку если её нет
#     Path(f'files/{message.chat.id}/photos').mkdir(parents=True, exist_ok=True)
#
#     # сохраним изображение
#     file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
#     downloaded_file = bot.download_file(file_info.file_path)
#     src = f'files/{message.chat.id}/' + file_info.file_path
#     with open(src, 'wb') as new_file:
#         new_file.write(downloaded_file)
#
#     # явно указано имя файла!
#     # откроем файл на чтение  преобразуем в base64
#     with open(f'files/{message.chat.id}/photos/file_0.jpg', "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read())
#
#     # откроем БД и запишем информацию (ID пользователя, base64, подпись к фото)
#     conn = sqlite3.connect("test.db")
#     cursor = conn.cursor()
#     cursor.execute('INSERT INTO users VALUES (?, ?, ?)', (message.chat.id, encoded_string, str(message.caption)))
#     conn.commit()
#
#
# # при получении команды /img от пользователя
# @bot.message_handler(commands=['img'])
# def ext_photo(message):
#     # откроем БД и по ID пользователя извлечём данные base64
#     conn = sqlite3.connect("test.db")
#     img = conn.execute('SELECT img FROM users WHERE tlgrm_id = ?', (message.chat.id,)).fetchone()
#     if img is None:
#         conn.close()
#         return None
#     else:
#         conn.close()
#
#         # сохраним base64 в картинку и отправим пользователю
#         with open("files/imageToSave.jpg", "wb") as fh:
#             fh.write(base64.decodebytes(img[0]))
#             bot.send_photo(message.chat.id, open("files/imageToSave.jpg", "rb"))
