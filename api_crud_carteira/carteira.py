import requests
import json
from datetime import datetime
from api_crud_carteira.sites_infos import *

url_base = HEROKU_API_CRUD
criar_acao = url_base + '/carteira'
del_acao = url_base +'/carteira'
info_carteira = url_base + '/usuarios'

def adicionar_acao(id_usuario, acao, preco_medio, stop_loss, stop_gain):
    new_acao_id = str(datetime.now()).replace('-','').replace(':','').replace('.','').replace(' ','')[::-1][:6]
    endpoint = f'{criar_acao}/{new_acao_id}'
    add_acao = {'acao':f'{acao}',
                'preco_medio':f'{preco_medio}',
                'stop_gain':f'{stop_loss}',
                'stop_loss':f'{stop_gain}',
                'usuario':f'{id_usuario}'
                }
    add_acao_carteira = requests.request('POST', endpoint, json=add_acao)
    return add_acao_carteira


def deletar_acao(id_usuario, acao):
    acao = acao.lower()
    id_usuario = int(id_usuario)
    endpoint = f'{info_carteira}/{id_usuario}'
    resposta = requests.request('GET', endpoint)
    resposta_json = resposta.json()
    acao_id = resposta_json['carteira']
    for retorno in acao_id:
        if retorno['acao'] == acao:
            acao_apagar = retorno['acao_id']
            endpoint = f'{del_acao}/{acao_apagar}'
            deletar_acao = requests.request('DELETE', endpoint)
    return acao

def pesquisar_carteira(id_usuario):
    lista_retorno = []
    endpoint = f'{info_carteira}/{id_usuario}'
    resposta = requests.request('GET', endpoint)
    carteira_json = resposta.json()
    carteira_json = carteira_json['carteira']
    for index in carteira_json:
        carteira_acao = []
        acao = index['acao']
        preco = index['preco_medio']
        stop_gain = index['stop_gain']
        stop_loss = index['stop_loss']
        carteira_acao.append(acao)
        carteira_acao.append(preco)
        carteira_acao.append(stop_loss)
        carteira_acao.append(stop_gain)
        lista_retorno.append(carteira_acao)
    return lista_retorno
