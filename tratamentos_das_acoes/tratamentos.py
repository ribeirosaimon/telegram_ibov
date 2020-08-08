
from telegram_bot.token_api import CHAT_ID
#busca a informação e faz o tratamento

def tratamentos(acao_json):
    analise_fundamentalista=acao_json['fundamentalist_analysis']
    fechamento = analise_fundamentalista['adj_close']
    print(fechamento)


def scheduler(context):
    context.bot.send_message(CHAT_ID, 'testando pra ver se da tudo certo')
