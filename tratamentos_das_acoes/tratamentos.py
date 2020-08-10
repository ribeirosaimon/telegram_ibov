
#busca a informação e faz o tratamento
from api_crud_carteira.carteira import pesquisar_carteira
from api_cotacao_bolsa.pegando_cotacao import *
from tratamentos_das_acoes.tratamento_hora_do_dia import *
import time
#[nome_acao, adj_close, high, low, avg_vol, vol, mov_avg, rsi]
ultima_referencia = ['',]
lista_de_mensagens = ['',]
minutos_atuais = int(datetime.now().strftime('%M'))

def tratamentos(chat_id):
    #chat_id=context.job.context
    carteira_acao = pesquisar_carteira(chat_id)
    for acao in carteira_acao:
        nome_acao_da_carteira = acao[0].upper()
        preco_acao_da_carteira = acao[1]
        api_rest=buscar_json_da_acao(nome_acao_da_carteira)
        preco_atual = api_rest['fundamentalist_analysis']['adj_close']
        print(preco_acao_da_carteira)
        print(preco_atual)

        if preco_acao_da_carteira <= preco_atual:
            codigo = f'{nome_acao_da_carteira}_adj_close{minutos_atuais}'
            print(lista_de_mensagens)
            for retorno in lista_de_mensagens:
                print(retorno)
                if codigo[:10] not in retorno[:10]:
                    print(f"Sua Ação {nome_acao_da_carteira} está com o preço maior que o indicado")
                    lista_de_mensagens.append(codigo)

        if preco_atual >= api_rest['fundamentalist_analysis']['high']:
            codigo = f'{nome_acao_da_carteira}_high{minutos_atuais}'
            for retorno in lista_de_mensagens:
                if codigo[:10] not in retorno[:10]:
                    print(f'Sua Ação {nome_acao_da_carteira} está na máxima do dia')
                    lista_de_mensagens.append(codigo)

        if preco_atual <= api_rest['fundamentalist_analysis']['low']:
            codigo = f'{nome_acao_da_carteira}_low{minutos_atuais}'
            for retorno in lista_de_mensagens:
                if codigo[:10] not in retorno[:10]:
                    print(f'Sua Ação {nome_acao_da_carteira} está na mínima do dia')
                    lista_de_mensagens.append(codigo)

        if api_rest['fundamentalist_analysis']['avg_vol'] / 7 < api_rest['fundamentalist_analysis']['vol'] / horas_pasadas_do_dia(datetime.now().strftime('%H')):
            codigo = f'{nome_acao_da_carteira}_vol{minutos_atuais}'
            for retorno in lista_de_mensagens:
                if codigo[:10] not in retorno[:10]:
                    print(f'O volume de sua ação {nome_acao_da_carteira} está acima do projetado')
                    lista_de_mensagens.append(codigo)

        if api_rest['technical_analysis']['%_last_reference'] >= 5:
            preco=api_rest['technical_analysis']['%_last_reference']
            referencia=api_rest['technical_analysis']['reference']
            if referencia == 'top':
                referencia = 'Topo'
            if referencia == 'bottom':
                referencia = 'Fundo'
            codigo = f'{nome_acao_da_carteira}_%_last_reference{minutos_atuais}'
            for retorno in lista_de_mensagens:
                if codigo[:10] not in retorno[:10]:
                    print(f'Sua Ação {nome_acao_da_carteira} com o a diferença de {preco}% do ultimo {referencia}')
                    lista_de_mensagens.append(codigo)

        if api_rest['technical_analysis']['call_hilo'] != ultima_referencia[-1]:
            codigo = f'{nome_acao_da_carteira}_hilo{minutos_atuais}'
            indicador_hilo = api_rest['technical_analysis']['call_hilo']
            del(ultima_referencia[:])
            ultima_referencia.append(indicador_hilo)
            if indicador_hilo == 'buy':
                indicador_hilo = 'Compra'
            if indicador_hilo == 'sell':
                indicador_hilo = 'Venda'
            for retorno in lista_de_mensagens:
                if codigo[:10] not in retorno[:10]:
                    print(f'O indicador HiLo da sua Ação {nome_acao_da_carteira} está indicando {indicador_hilo}')
                    del(ultima_referencia[:])
                    ultima_referencia.append(indicador_hilo)
                    lista_de_mensagens.append(codigo)
                    time.sleep(20)


        if api_rest['technical_analysis']['mov_avg'] >= preco_atual:
            codigo = f'{nome_acao_da_carteira}_mov_avg{minutos_atuais}'
            for retorno in lista_de_mensagens:
                if codigo[:10] not in retorno[:10]:
                    print(f'Sua Ação {nome_acao_da_carteira} está no mesmo valor que a MMA de 14 periodos, cotada agora à {preco_atual}')
                    lista_de_mensagens.append(codigo)



    print('ok')


    # Conferencia se os preços estão passando em todos os indicadores, e se o codigo[:10] está funcionando
