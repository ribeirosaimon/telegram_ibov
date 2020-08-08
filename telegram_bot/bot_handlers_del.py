from api_crud_carteira.carteira import *
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from api_crud_carteira.criar_carteira_db import criar_carteira_db
from telegram import ReplyKeyboardMarkup,ReplyKeyboardRemove,InlineKeyboardMarkup,InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import threading
import time


STAGE1_DEL = range(1)
CHAT_TIMEOUT=60
lista_acao_del = []


def start_del(update, context):
    update.message.reply_text('Digite a Ação que queira DELETAR')
    lista_acao_del.append(update.message.chat.id)
    return STAGE1_DEL




def stage1_del(update,context):
    lista_acao_del.append(update.message.text)
    deletar_acao(lista_acao_del[0],lista_acao_del[1])
    update.message.reply_text('Ação deletada!')
    return ConversationHandler.END

def cancel():
    update.message.reply_text('Comando Cancelado')

def timeout(update, context):
   update.message.reply_text('Ta beleza então, Abraços')
