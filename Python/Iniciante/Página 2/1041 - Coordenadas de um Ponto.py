# -*- coding: utf-8 -*-

coordenadas = list(map(float, input().split()))
if coordenadas[0] == 0 and coordenadas[1] == 0:
    print('Origem')
elif coordenadas[1] == 0:
    print("Eixo X")
elif coordenadas[0] == 0:
    print("Eixo Y")
else:
    if coordenadas[0] > 0 and coordenadas[1] > 0:
        print('Q1')
    elif coordenadas[0] < 0 and coordenadas[1] > 0:
        print('Q2')
    elif coordenadas[0] < 0 and coordenadas[1] < 0:
        print('Q3')
    elif coordenadas[0] > 0 and coordenadas[1] < 0:
        print('Q4')
