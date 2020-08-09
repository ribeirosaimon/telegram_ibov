from datetime import datetime

def horas_pasadas_do_dia(hora):
    hora = int(hora)
    if 10 <= hora <= 17:
        return hora % 10
    return 7
