

def olaMundo(bot, update):
    id_chat = update.message.chat_id
    bot.send_message(chat_id=id_chat, text='Olá Mundo')

def pegando_cotacao(bot, update):
    id_chat = update.message.chat_id
    bot.send_message(chat_id=id_chat, text='Olá Mundo')
