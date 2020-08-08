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
    carteira_acao = pesquisar_carteira(chat_id)
    for acao in carteira_acao:
        nome_acao_da_carteira = acao[0]
        preco_acao_da_carteira = acao[1]
        api_rest=buscar_json_da_acao(nome_acao_da_carteira)
        if preco_acao_da_carteira <= api_rest['fundamentalist_analysis']['adj_close']:
            context.bot.send_message(chat_id=chat_id,
                                     text=f"Sua Ação {nome_acao_da_carteira} está com o preço maior que o indicado")
