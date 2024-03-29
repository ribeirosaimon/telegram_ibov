import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
from telegram_bot.bot_handlers import *
from telegram_bot.bot_handlers_del import *
from telegram_bot.bot_handlers_carteira import *
from telegram_bot.bot_handlers_schedule import *
from api_crud_carteira.carteira import *
from telegram import bot
import os


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)
#from token_api import KEY
KEY = os.environ.get('KEY')

def main():
    updater = Updater(KEY, use_context=True)
    dp = updater.dispatcher
    updater.dispatcher.add_handler(CommandHandler('start', welcome))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex('Carteira'), minha_carteira))
    conv_handler_add = ConversationHandler(
        entry_points=[CommandHandler('Adicionar', start)],
        states={
            STAGE1: [MessageHandler(Filters.text, stage1)],
            STAGE2: [MessageHandler(Filters.text, stage2)],
            STAGE3: [MessageHandler(Filters.text, stage3)],
            STAGE4: [MessageHandler(Filters.text, stage4)],
            ConversationHandler.TIMEOUT: [MessageHandler(Filters.text | Filters.command, timeout)],
        },
        fallbacks=[CommandHandler('Cancel', cancel),],
        conversation_timeout=CHAT_TIMEOUT
    )
    dp.add_handler(conv_handler_add)
    # Remover ação
    conv_handler_del = ConversationHandler(
        entry_points=[CommandHandler('Deletar', start_del)],
        states={
            STAGE1_DEL: [MessageHandler(Filters.text, stage1_del)],
            STAGE2_DEL: [MessageHandler(Filters.text, stage2_del)],
            STAGE3_DEL: [MessageHandler(Filters.text, stage3_del)],
            STAGE4_DEL: [MessageHandler(Filters.text, stage4_del)],
            ConversationHandler.TIMEOUT: [MessageHandler(Filters.text | Filters.command, timeout)],
        },
        fallbacks=[CommandHandler('Cancel', cancel),],
        conversation_timeout=CHAT_TIMEOUT
    )
    dp.add_handler(conv_handler_del)
    dp.add_handler(CommandHandler("Acompanhe",acompanhe, pass_job_queue=True))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
