# -*- coding: utf-8 -*-

lista = list(map(int, input().split()))
inicial = lista[0] * 60 + lista[1]
final = lista[2] * 60 + lista[3]

if inicial < final:
    duracao = final - inicial
else:
    duracao = (1440 - inicial) + final

horas = duracao // 60
minutos = duracao % 60

print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')
