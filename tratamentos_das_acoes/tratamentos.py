
#busca a informação e faz o tratamento
from api_crud_carteira.carteira import pesquisar_carteira
from api_cotacao_bolsa.pegando_cotacao import *
from tratamentos_das_acoes.tratamento_hora_do_dia import *
import time
#[nome_acao, adj_close, high, low, avg_vol, vol, mov_avg, rsi]
'''
ultima_referencia = []
lista_de_mensagens = []


def envio_de_mensagem(texto, codigo):
    if not [item for item in lista_de_mensagens if item.startswith(codigo[:8])]:
        lista_de_mensagens.append(codigo)
        print(texto)


def tratamentos(chat_id):
    #chat_id=context.job.context
    minutos_atuais = datetime.now().strftime('%H')
    carteira_acao = pesquisar_carteira(chat_id)

    if len(lista_de_mensagens) == 0:
        pass
    else:
        for mensagem in lista_de_mensagens:
            tempo_de_envio = abs(int(mensagem[-2:]) - int(minutos_atuais))
            if tempo_de_envio >= 1:
                lista_de_mensagens.remove(mensagem)


    for acao in carteira_acao:
        nome_acao_da_carteira = acao[0].upper()
        preco_acao_da_carteira = acao[1]
        api_rest=buscar_json_da_acao(nome_acao_da_carteira)
        preco_atual = api_rest['fundamentalist_analysis']['adj_close']
        avg_vol = api_rest['fundamentalist_analysis']['avg_vol']
        vol = api_rest['fundamentalist_analysis']['vol']
        mov_avg = api_rest['technical_analysis']['mov_avg']
        ultima_referencia.append(api_rest['technical_analysis']['call_hilo'])

        if preco_acao_da_carteira <= preco_atual:
            codigo = f'{nome_acao_da_carteira}_adj_close{minutos_atuais}'
            envio_de_mensagem(f"Sua Ação {nome_acao_da_carteira} está com o preço maior que o indicado", codigo)


        if preco_atual >= api_rest['fundamentalist_analysis']['high']:
            codigo = f'{nome_acao_da_carteira}_high{minutos_atuais}'
            envio_de_mensagem(f'Sua Ação {nome_acao_da_carteira} está na máxima do dia', codigo)

        if preco_atual <= api_rest['fundamentalist_analysis']['low']:
            codigo = f'{nome_acao_da_carteira}_low{minutos_atuais}'
            envio_de_mensagem(f'Sua Ação {nome_acao_da_carteira} está na mínima do dia', codigo)


        if avg_vol / 7 < vol / horas_pasadas_do_dia(datetime.now().strftime('%H')):
            codigo = f'{nome_acao_da_carteira}_vol_{minutos_atuais}'
            envio_de_mensagem(f'O volume de sua ação {nome_acao_da_carteira} está acima do projetado, o volume atual é de {vol} e a media de volume nos ultimos 60 dias é de {avg_vol}', codigo)


        if mov_avg >= preco_atual:
            codigo = f'{nome_acao_da_carteira}_mov_avg{minutos_atuais}'
            envio_de_mensagem(f'Sua Ação {nome_acao_da_carteira} está no mesmo valor que a MMA de 14 periodos, cotada agora à {preco_atual}', codigo)

        if api_rest['technical_analysis']['%_last_reference'] >= 5:
            preco=api_rest['technical_analysis']['%_last_reference']
            referencia=api_rest['technical_analysis']['reference']
            if referencia == 'top':
                referencia = 'Topo'
            if referencia == 'bottom':
                referencia = 'Fundo'
            codigo = f'{nome_acao_da_carteira}_%_last_reference{minutos_atuais}'
            envio_de_mensagem(f'Sua Ação {nome_acao_da_carteira} com o a diferença de {preco}% do ultimo {referencia}', codigo)

        if api_rest['technical_analysis']['call_hilo'] != ultima_referencia[-1]:
            codigo = f'{nome_acao_da_carteira}_hilo{minutos_atuais}'
            indicador_hilo = api_rest['technical_analysis']['call_hilo']
            if indicador_hilo == 'buy':
                indicador_hilo = 'Compra'
            if indicador_hilo == 'sell':
                indicador_hilo = 'Venda'
            ultima_referencia.append(indicador_hilo)
            envio_de_mensagem(f'O indicador HiLo da sua Ação {nome_acao_da_carteira} está indicando {indicador_hilo}', codigo)

        if api_rest['technical_analysis']['rsi'] >= 70:
            codigo = f'{nome_acao_da_carteira}_rsi{minutos_atuais}'
            envio_de_mensagem(f'Cuidado, o indicador HiLo está em {api_rest['technical_analysis']['rsi']}', codigo)

        if api_rest['technical_analysis']['rsi'] <= 30:
            codigo = f'{nome_acao_da_carteira}_rsi{minutos_atuais}'
            envio_de_mensagem(f'O indicador HiLo está em {api_rest['technical_analysis']['rsi']}', codigo)
'''

    # Conferencia se os preços estão passando em todos os indicadores, e se o codigo[:10] está funcionando
