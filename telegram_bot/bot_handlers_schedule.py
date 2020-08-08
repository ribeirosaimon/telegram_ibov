from telegram.ext import Updater,CommandHandler
from telegram.ext import  MessageHandler,Filters,InlineQueryHandler
from tratamentos_das_acoes.tratamentos import *
import telegram


def acompanhe(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                     text="Estamos de Olho pra você")
    context.job_queue.run_repeating(callback_minute, interval=10, first=30,
                                    context=update.message.chat_id)


def callback_minute(context):
    chat_id=context.job.context
    tratamentos(chat_id)
    context.bot.send_message(chat_id=chat_id,
                             text="Hi User, Add Fund to your account to start trading")
