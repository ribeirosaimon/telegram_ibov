from api_crud_carteira.carteira import *
from api_crud_carteira.criar_carteira_db import *
from telegram_bot.buscar_info import *
from tratamentos_das_acoes.tratamentos import *

id_usuario = 883934505
acao = 'movi3'
json_acao = buscar_adj_close(acao)
tratamentos(json_acao)
