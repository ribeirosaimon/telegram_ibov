def tratamentos(acao_json):
    analise_fundamentalista=acao_json['fundamentalist_analysis']
    fechamento = analise_fundamentalista['adj_close']
    print(fechamento)
