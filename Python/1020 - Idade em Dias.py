valor = int(input())

ano, mes, dia = 0, 0, 0
while valor > 0:
    if valor >= 365:
        ano = valor // 365
        valor -= ano * 365
    elif valor >= 30:
        mes = valor // 30
        valor -= mes * 30
    else:
        dia = valor
        valor = 0

print(f'{ano} ano(s)\n{mes} mes(es)\n{dia} dia(s)')
