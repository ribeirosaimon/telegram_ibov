from api_crud_carteira.carteira import *


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def adicionar_acao(update, context):
    api_get = pegar_informacao()
    update.message.reply_text(f"Sua acao é {api_get['acao']} e seu preço Medio é de {api_get['preco_medio']}")

def informacoes_das_acoes(update,context):
    api_crud = pegar_informacao()
    print(api_crud['acao'])
    api_get = informacoes_acao(api_crud['acao'])
    update.message.reply_text(f"Sua acao esta indicando: {api_get[0]} pela HiLo")
    update.message.reply_text(f"E o RSI esta em {api_get[1]}%")
