import requests
import json
from datetime import datetime


url_base = 'http://localhost:5000'
criar_acao = url_base + '/carteira/'


def adicionar_acao(id_usuario, acao, preco_medio):
    new_id = str(datetime.now()).replace('-','').replace(':','').replace('.','').replace(' ','')[::-1][:10]
    endpoint = criar_acao +new_id + str(id_usuario)
    add_acao = {'acao':str(acao),
                'preco_medio':preco_medio,
                'usuario':int(id_usuario)
                }
    add_acao_carteira = requests.request('POST', endpoint, json=add_acao)
    return add_acao_carteira


def deletar_acao(acao, id_usuario):
    pass
