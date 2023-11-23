from pprint import pprint
import json

from django.conf import settings
import telebot
from math import *
from random import *

TOKEN = 'your_token_here'
bot = telebot.TeleBot(settings.TELEGRAM_BOT_API_KEY)
t = {}
c = {}
m = {}
b = {}
u = {}
p = {}

@bot.message_handler(commands=['игра'])
def start_game(message):
    chat_id = message.chat.id
    name = message.from_user.first_name
    bot.send_message(chat_id, f'Добро пожаловать, {name}, в числовую угадайку!')
    print(name)
    bot.send_message(chat_id, 'Введи свое имя:')
    bot.register_next_step_handler(message, get_name)


def get_name(message):
    print(message.text)
    global t
    t[message.chat.id] = message.text

    chat_id = message.chat.id
    name = t[message.chat.id]
    bot.send_message(chat_id, f'Привет, {name}! Введи предел:')
    print(message.chat.id)

    bot.register_next_step_handler(message, get_limit)


def get_limit(message):

    chat_id = message.chat.id
    global t
    global c
    global m
    global b
    global u
    global p

    name = t[message.chat.id]
    p[message.chat.id]=message.text
    p[message.chat.id]=str(p[message.chat.id])
    print(p[message.chat.id])
    try:

        p[message.chat.id] = int(message.text)

        u[message.chat.id]  = randint(1, p[message.chat.id])

        bot.send_message(chat_id, f'Mаксимально попыток по формуле log({p[message.chat.id]},2): {ugaday(p[message.chat.id])}')
        c[message.chat.id] = 1
        m[message.chat.id] = 1
        b[message.chat.id] = p[message.chat.id]

        bot.send_message(chat_id, f'{name}, введи число от {m[message.chat.id]} до {b[message.chat.id]}:')
        bot.register_next_step_handler(message, make_guess)


    except ValueError:
        bot.send_message(chat_id, f'{name}, введи целое число!')
        bot.register_next_step_handler(message, get_limit)
        return



def make_guess(message):
    global t
    global c
    global m
    global b
    global u
    global p
    chat_id = message.chat.id
    name = t[message.chat.id]
    num = message.text


    if not is_valid(num,message):
        bot.send_message(chat_id, f'{name}, а может быть все-таки введем целое число от {m[message.chat.id]} до {b[message.chat.id]}?')
        bot.register_next_step_handler(message, make_guess)
        return

    num = int(num)

    i=u[message.chat.id]
    if num < int(i):
        bot.send_message(chat_id, f'{name}, число меньше загаданного, введи число от {num} до {b[message.chat.id]}')
        c[message.chat.id] += 1
        m[message.chat.id] = num
        bot.register_next_step_handler(message, make_guess)
    elif num > int(i):
        bot.send_message(chat_id, f'{name}, число больше загаданного, введи число от {m[message.chat.id]} до {num}')
        c[message.chat.id] += 1
        b[message.chat.id] = num
        bot.register_next_step_handler(message, make_guess)
    else:
        bot.send_message(chat_id, f'{name}, ты угадал с {c[message.chat.id]} попытки(ок). Поздравляем!')
        print(c[message.chat.id])
        bot.send_message(chat_id, f'{name}, спасибо, что играл в числовую угадайку.')
        bot.send_message(chat_id, 'Сыграем еще раз? Напиши д (да) или н (нет):')

        bot.register_next_step_handler(message, play_again)


def play_again(message):
    global t
    chat_id = message.chat.id
    name = t[message.chat.id]
    i = message.text
    s=str(i)
    i=s.lower()


    if i.startswith('д' or 'Д'):
        bot.send_message(chat_id, f'{name}, введи новый предел:')
        bot.register_next_step_handler(message, get_limit)
    else:
        bot.send_message(chat_id, f'До свидания, {name}! Скажи АлЁше, что он МОЛОДЕЦ!')


def is_valid(argument,message):
    global p
    x=p[message.chat.id]
    x=int(x)
    try:
        number = int(argument)
        if 1 <= number <= x:
            return True
        else:
            return False
    except:
        return False


def ugaday(n):
    if int(log(n, 2)) == log(n, 2):
        n = int(log(n, 2))
    else:
        n = int(log(n, 2)) + 1
    return n


import time
import requests.exceptions
from urllib3.exceptions import ProtocolError
# while True:
#     try:
#         bot.polling()
#     except requests.exceptions.ReadTimeout:
#         time.sleep(30)
while True:
    try:
        bot.polling(none_stop=True)

    except (ConnectionResetError, ProtocolError) as e:
        # Запись в лог или просто печать ошибки
        print(e)

        # Пауза перед следующей попыткой
        time.sleep(15)