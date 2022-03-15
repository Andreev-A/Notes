# 1961796256:AAGeSMjx2sO8hGQq8biD_8ZAInuj3dOe4II    @Apower_TODO_bot
# 5268671568:AAF9DTbcJZkWcdJVhAHJR0BqhhAakInDhAI    t.me/apower_bot.
import telebot


TOKEN = '5268671568:AAF9DTbcJZkWcdJVhAHJR0BqhhAakInDhAI'

bot = telebot.TeleBot(TOKEN, parse_mode=None)  # Вы можете установить parse_mode по умолчанию. HTML или MARKDOWN

# memory
from collections import defaultdict

START, TITLE, PRICE, CONFIRMATION = range(4)
USER_STATE = defaultdict(lambda: START)


def get_state(message):
    return USER_STATE[message.chat.id]


def update_state(message, state):
    USER_STATE[message.chat.id] = state

@bot.message_handler(func=lambda message: get_state(message) == START)
def handle_message(message):
    bot.send_message(message.chat.id, text='Напишите название')
    update_state(message, TITLE)


@bot.message_handler(func=lambda message: get_state(message) == TITLE)
def handle_title(message):
    # название
    update_product(message.chat.id, 'title', message.text)
    bot.send_message(message.chat.id, text='Укажи цену')
    update_state(message, PRICE)


@bot.message_handler(func=lambda message: get_state(message) == PRICE)
def handle_price(message):
    update_product(message.chat.id, 'price', message.text)
    product = get_product(message.chat.id)
    bot.send_message(message.chat.id, text='Опубликовать объявление? {}'.format(product))
    update_state(message, CONFIRMATION)


@bot.message_handler(func=lambda message: get_state(message) == CONFIRMATION)
def handle_confirmation(message):
    if 'да' in message.text.lower():
        bot.send_message(message.chat.id, text='Объявление опубликовано')
    update_state(message, START)


PRODUCTS = defaultdict(lambda: {})

def update_product(user_id, key, value):
    PRODUCTS[user_id][key] = value

def get_product(user_id):
    return PRODUCTS[user_id]


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


bot.polling()


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
#   bot.send_message(message.chat.id, 'Скажи сколько игроков с тобой будет играть (только числами! И от 5 до 10 игроков)?')
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
