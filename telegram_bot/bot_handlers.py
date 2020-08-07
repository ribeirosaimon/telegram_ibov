from api_crud_carteira.carteira import *
from telegram.replykeyboardmarkup import ReplyKeyboardMarkup

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help_command(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def welcome(update, context):
    kbd_layout = [
        ['📥Adicionar Ação'],
        ['📤Deletar Ação'],
        ['📈Minha carteira']
    ]

    kbd = ReplyKeyboardMarkup(kbd_layout)
    update.message.reply_text(text='Olá, ' + update.message.from_user.first_name +'!', reply_markup=kbd)
    id_usuario = update['message']['chat']['id']



def add_acao(update, context):
   update.message.reply_text("Função de deposito")


def del_acao(update, context):
   update.message.reply_text("Função de retirada")

def minha_carteira(update, context):
   update.message.reply_text("Função de pagamentos")
