from api_crud_carteira.carteira import *
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from api_crud_carteira.criar_carteira_db import criar_carteira_db
from telegram import ReplyKeyboardMarkup,ReplyKeyboardRemove,InlineKeyboardMarkup,InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import threading
import time


STAGE1, STAGE2 = range(2)
CHAT_TIMEOUT=60
lista_acao = []



def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)



def remider(update,context):
    for i in range(int(CHAT_TIMEOUT / 2)):
        thread_state=context.user_data['thread']
        print(i)
        if thread_state:
            time.sleep(1)
        else:
            break
    if thread_state:
        update.message.reply_text('only 30 seconds left. Please Hurry!')


def welcome(update, context):
    kbd_layout = [
        ['/Adicionar'],
        ['/Deletar'],
        ['/Carteira']
    ]

    kbd = ReplyKeyboardMarkup(kbd_layout)
    update.message.reply_text(text='Olá, ' + update.message.from_user.first_name +'!', reply_markup=kbd)
    id_usuario = int(update.message.chat.id)
    try:
        criar_carteira_db(id_usuario)
    except:
        pass


def add_acao(update, context):

   id_usuario = int(update['message']['chat']['id'])
   adicionar_acao(acao,id_usuario,preco_medio)


def del_acao(update, context):
   update.message.reply_text("Função de retirada")

def minha_carteira(update, context):
   update.message.reply_text("Função de pagamentos")


def start(update, context):
    update.message.reply_text('Olá, digite o nome de uma ação para adicionar a sua carteira')
    lista_acao.append(update.message.chat.id)
    return STAGE1

def stage1 (update,context):
    update.message.reply_text('Agora me fale o valor que quer receber alerta')
    lista_acao.append(update.message.text)
    return STAGE2


def stage2(update,context):
    lista_acao.append(float(update.message.text))
    adicionar_acao(lista_acao[0],lista_acao[1],lista_acao[2])
    update.message.reply_text('Tudo adicionado! qualquer informação vou te retornar')
    del(lista_acao[:])
    return ConversationHandler.END

def cancel():
    pass

def timeout(update, context):
   update.message.reply_text('Ta beleza então, Abraços')
