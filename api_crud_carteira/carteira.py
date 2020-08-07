import requests
import json

url_base = 'http://localhost:5000'
carteira = url_base + '/carteira/0'


acao={
'acao':'movi3',
'preco_medio':15.80
}

print(url_base+carteira)
