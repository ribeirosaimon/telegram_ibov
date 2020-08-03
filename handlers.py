def olaMundo(bot, update):
    id_chat = update.message.chat_id
    print(id_chat)
    bot.send_message(chat_id=id_chat, text='Olá Mundo')
