import requests
import json
from api_crud_carteira.sites_infos import *

url_base = HEROKU_API_CRUD
criar_carteira = url_base + '/usuarios/'

def criar_carteira_db(id_telegram):
    endpoint = criar_carteira + str(id_telegram)
    usuario_id = {'usuario':int(id_telegram)}
    resposta_usuario = requests.request('POST', endpoint, json=usuario_id)
    return resposta_usuario
