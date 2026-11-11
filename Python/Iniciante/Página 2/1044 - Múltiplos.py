# -*- coding: utf-8 -*-

lista = sorted(list(map(int, input().split())), reverse=True)
if lista[0] % lista[1] == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
