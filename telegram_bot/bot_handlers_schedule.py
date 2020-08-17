from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler
from tratamentos_das_acoes.tratamentos import *
import telegram

ultima_referencia = []
lista_de_mensagens = []
referencia_top_ou_bot = []
'''

def acompanhe(update, context):
    horario_atual = int(datetime.now().strftime('%H'))
#    if horario_atual <= 17:
    context.bot.send_message(chat_id=update.message.chat_id,
                     text="Estamos de Olho pra você")
    context.job_queue.run_daily(callback_minute, time=time(hour=21, minute=17, seconds=0), days=(0, 1, 2, 3, 4, 5, 6), context=update.message.chat_id)
    #else:
    #    context.bot.send_message(chat_id=update.message.chat_id,
    #                     text="Fora do Horario do Pregão ")


'''
def acompanhe(update, context):
    horario_atual = int(datetime.now().strftime('%H'))
    if horario_atual < 18:
        context.bot.send_message(chat_id=update.message.chat_id, text="Estamos de Olho pra você")
        acompanhe_sms = context.job_queue.run_repeating(callback_minute, interval=30, first=0,context=update.message.chat_id, name='my_job')
    else:
        context.bot.send_message(chat_id=update.message.chat_id,
                         text="Fora do Horario do Pregão ")


def callback_minute(context: telegram.ext.CallbackContext):
    chat_id=context.job.context
    horario_atual = int(datetime.now().strftime('%H'))
    job = context.job
    if horario_atual >= 18:
        job.schedule_removal()
        context.bot.send_message(chat_id=chat_id,text='Bom por hoje é só!')

    def envio_de_mensagem(texto, codigo):
        if not [item for item in lista_de_mensagens if item.startswith(codigo[:8])]:
            lista_de_mensagens.append(codigo)
            context.bot.send_message(chat_id=chat_id,text=texto)


    minutos_atuais = datetime.now().strftime('%H')
    carteira_acao = pesquisar_carteira(chat_id)

    if len(lista_de_mensagens) == 0:
        pass
    else:
        for mensagem in lista_de_mensagens:
            tempo_de_envio = abs(int(mensagem[-2:]) - int(minutos_atuais))
            if tempo_de_envio > 2:
                lista_de_mensagens.remove(mensagem)


    for acao in carteira_acao:
        nome_acao_da_carteira = acao[0].upper()
        preco_acao_da_carteira = acao[1]
        stop_loss_carteira = acao[2]
        stop_gain_carteira = acao[3]
        api_rest=buscar_json_da_acao(nome_acao_da_carteira)
        preco_atual = api_rest['fundamentalist_analysis']['adj_close']
        avg_vol = api_rest['fundamentalist_analysis']['avg_vol']
        vol = api_rest['fundamentalist_analysis']['vol']
        mov_avg = api_rest['technical_analysis']['mov_avg']
        ultima_referencia.append(api_rest['technical_analysis']['call_hilo'])
        referencia_top_ou_bot.append(api_rest['technical_analysis']['reference'])
        rsi = api_rest['technical_analysis']['rsi']

        if stop_gain_carteira <= preco_atual:
            codigo = f'{nome_acao_da_carteira}_adj_close{minutos_atuais}'
            envio_de_mensagem(f"Sua Ação {nome_acao_da_carteira} atingiu o Stop Gain à {preco_atual}", codigo)


        if stop_loss_carteira >= preco_atual:
            codigo = f'{nome_acao_da_carteira}_adj_close{minutos_atuais}'
            envio_de_mensagem(f"Sua Ação {nome_acao_da_carteira} atingiu o Stop Loss à {preco_atual}", codigo)


        if preco_atual >= api_rest['fundamentalist_analysis']['high']:
            codigo = f'{nome_acao_da_carteira}_high{minutos_atuais}'
            envio_de_mensagem(f'Sua Ação {nome_acao_da_carteira} está na máxima do dia, cotada agora à {preco_atual}', codigo)


        if preco_atual <= api_rest['fundamentalist_analysis']['low']:
            codigo = f'{nome_acao_da_carteira}_low{minutos_atuais}'
            envio_de_mensagem(f'Sua Ação {nome_acao_da_carteira} está na mínima do dia, cotada agora à {preco_atual}', codigo)


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

        if rsi >= 70:
            codigo = f'{nome_acao_da_carteira}_rsi{minutos_atuais}'
            envio_de_mensagem(f'Cuidado, o RSI está em {rsi}%', codigo)

        if rsi <= 30:
            codigo = f'{nome_acao_da_carteira}_rsi{minutos_atuais}'
            envio_de_mensagem(f'O indicador RSI está em {rsi}%', codigo)


        if api_rest['technical_analysis']['reference'] != referencia_top_ou_bot[-1]:
            codigo = f'{nome_acao_da_carteira}_reference{minutos_atuais}'
            reference = api_rest['technical_analysis']['reference']
            if reference == 'top':
                reference = 'Topo'
            if reference == 'bottom':
                reference = 'Fundo'
            referencia_top_ou_bot.append(reference)
            envio_de_mensagem(f'Sua Ação: {nome_acao_da_carteira} está fazendo novo {reference}', codigo)
