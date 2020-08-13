from api_crud_carteira.carteira import *
from api_crud_carteira.criar_carteira_db import *
from api_cotacao_bolsa.pegando_cotacao import *
from tratamentos_das_acoes.tratamentos import *
from tratamentos_das_acoes.tratamento_hora_do_dia import *
import time



id_usuario = 883934505
acao = 'movi3'

retorno = pesquisar_carteira(id_usuario, acao)
print(retorno)
