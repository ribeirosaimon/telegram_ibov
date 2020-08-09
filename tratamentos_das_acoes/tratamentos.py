
#busca a informação e faz o tratamento
from api_crud_carteira.carteira import pesquisar_carteira
from api_cotacao_bolsa.pegando_cotacao import *
from tratamentos_das_acoes.tratamento_hora_do_dia import *

#[nome_acao, adj_close, high, low, avg_vol, vol, mov_avg, rsi]
ultima_referencia = ['',]
lista_de_mensagens = []

def tratamentos(chat_id):
    #chat_id=context.job.context
    carteira_acao = pesquisar_carteira(chat_id)
    for acao in carteira_acao:
        nome_acao_da_carteira = acao[0].upper()
        preco_acao_da_carteira = acao[1]
        api_rest=buscar_json_da_acao(nome_acao_da_carteira)
        preco_atual = api_rest['fundamentalist_analysis']['adj_close']

        if preco_acao_da_carteira <= preco_atual:
            codigo = f'{nome_acao_da_carteira}_adj_close'
            if codigo not in lista_de_mensagens:
                print(f"Sua Ação {nome_acao_da_carteira} está com o preço maior que o indicado")
                lista_de_mensagens.append(codigo)


        if preco_atual >= api_rest['fundamentalist_analysis']['high']:
            codigo = f'{nome_acao_da_carteira}_high'
            if codigo not in lista_de_mensagens:
                print(f'Sua Ação {nome_acao_da_carteira} está na máxima do dia')
                lista_de_mensagens.append(codigo)


        if preco_atual <= api_rest['fundamentalist_analysis']['low']:
            codigo = f'{nome_acao_da_carteira}_low'
            if codigo not in lista_de_mensagens:
                print(f'Sua Ação {nome_acao_da_carteira} está na mínima do dia')
                lista_de_mensagens.append(codigo)


        if api_rest['fundamentalist_analysis']['avg_vol'] / 7 < api_rest['fundamentalist_analysis']['vol'] / horas_pasadas_do_dia(datetime.now().strftime('%H')):
            codigo = f'{nome_acao_da_carteira}_vol'
            if codigo not in lista_de_mensagens:
                print(f'O volume de sua ação {nome_acao_da_carteira} está acima do projetado')
                lista_de_mensagens.append(codigo)

        if api_rest['technical_analysis']['%_last_reference'] >= 5:
            preco=api_rest['technical_analysis']['%_last_reference']
            referencia=api_rest['technical_analysis']['reference']
            if referencia == 'top':
                referencia = 'Topo'
            if referencia == 'bottom':
                referencia = 'Fundo'
            codigo = f'{nome_acao_da_carteira}_%_last_reference'
            if codigo not in lista_de_mensagens:
                print(f'Sua Ação {nome_acao_da_carteira} com o a diferença de {preco}% do ultimo {referencia}')
                lista_de_mensagens.append(codigo)


        if api_rest['technical_analysis']['call_hilo'] != ultima_referencia[-1]:
            codigo = f'{nome_acao_da_carteira}_hilo'
            indicador_hilo = api_rest['technical_analysis']['call_hilo']
            if indicador_hilo == 'buy':
                indicador_hilo = 'Compra'
            if indicador_hilo == 'sell':
                indicador_hilo = 'Venda'
            if codigo not in lista_de_mensagens:
                print(f'O indicador HiLo da sua Ação {nome_acao_da_carteira} está indicando {indicador_hilo}')
                del(ultima_referencia[:])
                ultima_referencia.append(indicador_hilo)
                lista_de_mensagens.append(codigo)


        if api_rest['technical_analysis']['mov_avg'] >= preco_atual:
            codigo = f'{nome_acao_da_carteira}_mov_avg'
            if codigo not in lista_de_mensagens:
                print(f'Sua Ação {nome_acao_da_carteira} está no mesmo valor que a MMA de 14 periodos, cotada agora à{}')
                lista_de_mensagens.append(codigo)


    print('tudo passou ok!')
