from telegram_bot.sites_info import *
import requests

def buscar_adj_close(acao):
    endpoint = HEROKU_API_INFO+acao
    resposta = requests.request('GET', endpoint)
    resposta_da_acao = resposta.json()
    return resposta_da_acao[acao]
