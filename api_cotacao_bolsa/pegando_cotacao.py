import requests
from api_cotacao_bolsa.sites_infos import HEROKU_API_INFO
import time

def buscar_json_da_acao(acao):
    endpoint = f'{HEROKU_API_INFO}/{acao}'
    resposta = requests.request('GET', endpoint)
    time.sleep(1)
    resposta_da_acao = resposta.json()
    resposta_da_acao = resposta_da_acao[acao]
    return resposta_da_acao
