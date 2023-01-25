import os

import requests
import telebot
from bs4 import BeautifulSoup

TOKEN = os.environ['TOKEN']
URL = 'https://www.sports.ru/roma/calendar/'
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)


def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()
