import telebot
import json
import os
import dotenv

# with open("data.json", "r") as fh:
#     users = json.load(fh)

# with open("data.json", "w") as fh:
#     json.dump([users, {4: 1}], fh

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, "Привет!")
    print(f'Start command used by {message.chat.username}')