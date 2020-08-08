from api_crud_carteira.carteira import *
from api_crud_carteira.criar_carteira_db import *
from telegram_bot.buscar_info import *
from telegram_bot.tratamentos import *

acao = buscar_informacoes('movi3')
tratamentos(acao)
