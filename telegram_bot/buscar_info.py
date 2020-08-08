from telegram_bot.sites_info import *
import requests

def buscar_json_da_acao(acao):
    endpoint = HEROKU_API_INFO+acao
    resposta = requests.request('GET', endpoint)
    resposta_da_acao = resposta.json()
    resposta_da_acao = resposta_da_acao[acao]
    analise_fundamentalista = resposta_da_acao['fundamentalist_analysis']
    analise_tecnica = resposta_da_acao['technical_analysis']
    return analise_fundamentalista, analise_tecnica
