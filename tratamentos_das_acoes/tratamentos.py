
#busca a informação e faz o tratamento
from api_crud_carteira.carteira import pesquisar_carteira

def tratamentos(id_usuario):
    carteira_acao = pesquisar_carteira(id_usuario)
    for acao in carteira_acao:
        nome_acao_da_carteira = acao[0]
        preco_acao_da_carteira = acao[1]
        buscar_json_da_acao(nome_acao_da_carteira)


    #info_aca = buscar_json_da_acao(acao)
