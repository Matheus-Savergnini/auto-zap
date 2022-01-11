import datetime


def hora_agora():
    hora = f'{datetime.datetime.now().hour}'
    if len(hora) < 2:
        hora = f'0{hora}'
    minuto = f'{datetime.datetime.now().minute}'
    if len(minuto) < 2:
        minuto = f'0{minuto}'
    tempo = f'{hora}:{minuto}'
    return tempo
