import requests
import json
from datetime import datetime
from api_crud_carteira.sites_infos import *

url_base = HEROKU_API_CRUD

url_base = HEROKU_API_CRUD
criar_acao = url_base + '/carteira/'
del_acao = url_base +'/usuarios/'
info_carteira = url_base + '/usuarios/'

def adicionar_acao(id_usuario, acao, preco_medio):
    new_id = str(datetime.now()).replace('-','').replace(':','').replace('.','').replace(' ','')[::-1][:10]
    endpoint = criar_acao +new_id + str(id_usuario)
    add_acao = {'acao':str(acao),
                'preco_medio':preco_medio,
                'usuario':int(id_usuario)
                }
    add_acao_carteira = requests.request('POST', endpoint, json=add_acao)
    return add_acao_carteira


def deletar_acao(id_usuario, acao):
    acao = acao.lower()
    id_usuario = int(id_usuario)
    endpoint = del_acao + str(id_usuario)
    resposta = requests.request('GET', endpoint)
    resposta_json = resposta.json()
    acao_id = resposta_json['carteira'][0]['acao_id']
    endpoint = criar_acao + str(acao_id)
    deletar_acao = requests.request('DELETE', endpoint)
    return deletar_acao

def pesquisar_carteira(id_usuario):
    lista_retorno = []
    endpoint = info_carteira + str(id_usuario)
    resposta = requests.request('GET', endpoint)
    carteira_json = resposta.json()
    carteira_json['carteira'][0]

    for index in range(len(carteira_json['carteira'])):
        acao = carteira_json['carteira'][index]['acao']
        preco = carteira_json['carteira'][index]['preco_medio']
        lista_retorno.append(f'Ação: {acao}     Preço Alerta: {preco}')
    return lista_retorno
