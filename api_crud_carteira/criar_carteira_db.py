import requests
import json

url_base = 'http://localhost:5000'
criar_carteira = url_base + '/usuario/'

def criar_carteira_db(id_telegram):
    endpoint = criar_carteira + str(id_telegram)
    usuario_id = {'usuario':id_telegram}
    resposta_usuario = requests.request('POST', endpoint, json=usuario_id)
    return resposta_usuario
