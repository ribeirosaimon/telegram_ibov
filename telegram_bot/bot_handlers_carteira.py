from api_crud_carteira.carteira import pesquisar_carteira

from telegram_bot.sites_info import *
import telegram.ext



def minha_carteira(update, context):
    id_usuario = int(update['message']['chat']['id'])
    carteira_usuario = pesquisar_carteira(id_usuario)
    for index in carteira_usuario:
        mensagem = f'Ação: {index[0]}     Preço Alerta: {index[1]}'
        update.message.reply_text(mensagem)
