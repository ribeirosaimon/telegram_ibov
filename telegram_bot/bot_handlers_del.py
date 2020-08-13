from api_crud_carteira.carteira import *
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup
from api_crud_carteira.criar_carteira_db import criar_carteira_db
from telegram import ReplyKeyboardMarkup,ReplyKeyboardRemove,InlineKeyboardMarkup,InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler
import threading
import time


STAGE1_DEL, STAGE2_DEL, STAGE3_DEL, STAGE4_DEL  = range(4)
CHAT_TIMEOUT=60
lista_acao_del = []


def start_del(update, context):
    update.message.reply_text('Digite a Ação que queira DELETAR')
    lista_acao_del.append(update.message.chat.id)
    return STAGE1_DEL

def stage1_del(update, context):
    lista_acao_del.append(update.message.text)
    update.message.reply_text(f'Qual o Valor que Deseja vender {lista_acao_del[1]}?')
    return STAGE2_DEL

def stage2_del(update, context):
    lista_acao_del.append(update.message.text)
    update.message.reply_text(f'Qual a quantidade da sua venda? isso é só pra calcular o IR, caso não queira somente digite 0')
    return STAGE3_DEL

def stage3_del(update, context):
    lista_acao_del.append(update.message.text)
    update.message.reply_text(f'Tem certeza que deseja vender {lista_acao_del[3]} {lista_acao_del[1]} a R${lista_acao_del[2]}')
    return STAGE4_DEL


def stage4_del(update,context):
    preco_medio = 0
    lista_acao_del.append(update.message.text)
    retorno = pesquisar_carteira(lista_acao_del[0])
    for acao in retorno:
        if acao[0] == lista_acao_del[1]:
            preco_medio = acao[1]
    lucro_por_acao = float(lista_acao_del[2] ) - float(preco_medio)
    lucro = float(lucro_por_acao) * float(lista_acao_del[3])
    imposto_de_renda = round(lucro * 0.15, 2)
    if lista_acao_del[4].lower() == 'sim':
        deletar_acao(lista_acao_del[0],lista_acao_del[1])
        update.message.reply_text(f'Ação {lista_acao_del[1]} vendida com lucro de R${round(lucro,2)}, seu IR é de {imposto_de_renda}')
    else:
        update.message.reply_text('Beleza, qualquer coisa comece novamente')
    del(lista_acao_del[:])
    return ConversationHandler.END


def timeout(update, context):
   update.message.reply_text('Ta beleza então, Abraços')
