
#busca a informação e faz o tratamento
from api_crud_carteira.carteira import pesquisar_carteira

def tratamentos(acao, id_usuario):
    [x[0] for x in pesquisar_carteira(id_usuario)]

    info_aca = buscar_json_da_acao(acao)
