import logging
from token_api import KEY
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram_bot.bot_handlers import *
from telegram import bot

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)




def main():
    updater = Updater(KEY, use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', welcome))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex(r"📥Adicionar Ação"), add_acao))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex(r"📤Deletar Açao"), del_acao))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex(r"📈Minha Carteira"), minha_carteira))

    dp = updater.dispatcher
    #dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
