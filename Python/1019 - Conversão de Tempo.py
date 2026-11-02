valor = int(input())

treshold_hora = 60 ** 2
hora, minuto, segundo = 0, 0, 0
while valor > 0:
    if valor >= treshold_hora:
        hora = valor // treshold_hora
        valor -= hora * treshold_hora
    elif valor >= 60:
        minuto = valor // 60
        valor -= minuto * 60
    else:
        segundo = valor
        valor = 0

print(f'{hora}:{minuto}:{segundo}')
