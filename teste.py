from telegram.ext import *
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup


def welcome(update, context):
    kbd_layout = [
        ['💵Saldo'], ['📥Depósito', '📤Retirada'],
        ['👥Equipe','✉️Ajuda'],['📈Canal De Pagamentos']
    ]

    kbd = ReplyKeyboardMarkup(kbd_layout)

    update.message.reply_text(text='Olá, ' + update.message.from_user.first_name +'!', reply_markup=kbd)

def echo(update, context):
   update.message.reply_text("Mensagem não mapeada recebida: %s" % update.message.text)

def saldo(update, context):
   update.message.reply_text("Função de saldo")

def deposito(update, context):
   update.message.reply_text("Função de deposito")

def retirada(update, context):
   update.message.reply_text("Função de retirada")

def equipe(update, context):
   update.message.reply_text("Função de equipe")

def ajuda(update, context):
   update.message.reply_text("Função de ajuda")

def pagamentos(update, context):
   update.message.reply_text("Função de pagamentos")

def main():
    updater = Updater(token="SEU TOKEN AQUI", use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', welcome))

    updater.dispatcher.add_handler(MessageHandler(Filters.regex(r"💵Saldo"), saldo))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex(r"📥Depósito"), deposito))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex(r"📤Retirada"), retirada))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex(r"👥Equipe"), equipe))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex(r"✉️Ajuda"), ajuda))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex(r"📈Canal De Pagamentos"), pagamentos))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex(r""), echo))

    updater.start_polling()
    print(str(updater))
    updater.idle()

if __name__ == '__main__':
    main()
