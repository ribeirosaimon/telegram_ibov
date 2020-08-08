
#busca a informação e faz o tratamento
from api_crud_carteira.carteira import pesquisar_carteira

def tratamentos(id_usuario):
    acao = pesquisar_carteira(id_usuario)
    print(acao)

    info_aca = buscar_json_da_acao(acao)
