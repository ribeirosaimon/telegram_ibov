from telegram.ext import Updater, CommandHandler
from handlers import *
from token_api import KEY


def main():
    updater = Updater(KEY)
    bot = updater.dispatcher
    bot.add_handler(CommandHandler('ola', olaMundo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
