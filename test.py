from api_crud_carteira.carteira import *
from api_crud_carteira.criar_carteira_db import *
from api_cotacao_bolsa.pegando_cotacao import *
from tratamentos_das_acoes.tratamentos import *
from tratamentos_das_acoes.tratamento_hora_do_dia import *
import time



id_usuario = 883934505
acao = 'movi3'

while True:
    tratamentos(id_usuario)
    time.sleep(10)


'''


eu quero fazer assim...
só adicionar na lista palavras que nao tem as 3 primeiras letras
tipo eu digito: meugrandeamigo

vai adicionar na lista

se eu digitar: meug
nao vai add na lista pq ja tem uma palavra com as 4 letras do mesmo jeito


my_list = []
var1 = 'my_best_friend'
while True:
    var1 = input('digite algo: ')
    if var1 not in my_list:
        my_list.append(var1)
        print(var1)
        time.sleep(0.5)
    print(my_list)
    time.sleep(0.5)



mi_list = ['Ruan', 'lucas', 'meu', 'grande', 'amigo']

while True:
    variavel = input('Digite um nome: ')
    for i in mi_list:
        if variavel[:2] in i[:2]:
            break
    else:
        print('n tem add agora!')
        mi_list.append(variavel)
    print(mi_list)
'''
