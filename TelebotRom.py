import os

import telebot

TOKEN = os.environ['TOKEN']

bot = telebot.TeleBot(token=TOKEN)


@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)


def main():
    bot.infinity_polling()


if __name__ == '__main__':
    main()
