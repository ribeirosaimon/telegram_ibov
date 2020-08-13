from api_crud_carteira.carteira import *
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from api_crud_carteira.criar_carteira_db import criar_carteira_db
from telegram import ReplyKeyboardMarkup,ReplyKeyboardRemove,InlineKeyboardMarkup,InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import threading
import time


STAGE1_DEL, STAGE2_DEL = range(2)
CHAT_TIMEOUT=60
lista_acao_del = []


def start_del(update, context):
    update.message.reply_text('Digite a Ação que queira DELETAR')
    lista_acao_del.append(update.message.chat.id)
    return STAGE1_DEL

def stage1_del(update, context):
    lista_acao_del.append(update.message.text)
    update.message.reply_text(f'Tem certeza que quer Vender {lista_acao_del[1]}')
    return STAGE2_DEL


def stage2_del(update,context):
    lista_acao_del.append(update.message.text)
    if lista_acao_del[2].lower() == 'sim':
        deletar_acao(lista_acao_del[0],lista_acao_del[1])
        update.message.reply_text(f'Ação {lista_acao_del[1]} deletada!')
    else:
        update.message.reply_text('Beleza, qualquer coisa comece novamente')
    return ConversationHandler.END


def timeout(update, context):
   update.message.reply_text('Ta beleza então, Abraços')
