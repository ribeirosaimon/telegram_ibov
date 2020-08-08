from api_crud_carteira.carteira import pesquisar_carteira


def minha_carteira(update, context):
    id_usuario = int(update['message']['chat']['id'])
    carteira_usuario = pesquisar_carteira(id_usuario)
    for index in carteira_usuario:
        update.message.reply_text(index)
