import requests
import json

url_base = 'http://localhost:5000'
carteira = url_base + '/carteira/0'

api_rest = 'https://secure-wildwood-34847.herokuapp.com/'

def pegar_informacao():
    resposta_get = requests.get(carteira)
    return resposta_get.json()


def informacoes_acao(acao):
    retorno = api_rest+str(acao)
    resposta = requests.get(retorno).json()
    call_hilo = resposta[f'{acao}']['technical_analysis']['call_hilo']
    rsi = resposta[f'{acao}']['technical_analysis']['rsi']
    return call_hilo, rsi
