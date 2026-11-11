# -*- coding: utf-8 -*-

lista = list(map(int, input().split()))
inicial = lista[0]
final = lista[1]

if inicial < final:
    horas = final - inicial
else:
    horas = 24 - inicial + final

print(f'O JOGO DUROU {horas} HORA(S)')
