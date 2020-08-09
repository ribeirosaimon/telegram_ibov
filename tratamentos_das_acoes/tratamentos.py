
#busca a informação e faz o tratamento
from api_crud_carteira.carteira import pesquisar_carteira
from api_cotacao_bolsa.pegando_cotacao import *

lista_de_mensagens = []

def tratamentos(chat_id):
    #chat_id=context.job.context
    carteira_acao = pesquisar_carteira(chat_id)
    for acao in carteira_acao:
        nome_acao_da_carteira = acao[0].upper()
        preco_acao_da_carteira = acao[1]
        api_rest=buscar_json_da_acao(nome_acao_da_carteira)
        if preco_acao_da_carteira <= api_rest['fundamentalist_analysis']['adj_close']:
            resposta = f"Sua Ação {nome_acao_da_carteira} está com o preço maior que o indicado"
            print(resposta)
            lista_de_mensagens.append(resposta)
        if api_rest['fundamentalist_analysis']['adj_close'] >= api_rest['fundamentalist_analysis']['high']:
            resposta = f'Sua Ação {nome_acao_da_carteira} está na máxima do dia'
            print(resposta)
            lista_de_mensagens.append(resposta)
        if api_rest['fundamentalist_analysis']['adj_close'] <= api_rest['fundamentalist_analysis']['low']:
            resposta = f'Sua Ação {nome_acao_da_carteira} está na mínima do dia'
            print(resposta)
            lista_de_mensagens.append(resposta)
