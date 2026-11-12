# -*- coding: utf-8 -*-

import sys

for entrada in sys.stdin:
    n = int(entrada)

    centro = n // 2
    borda_quadrado = n // 3

    for i in range(n):
        linha = []
        for j in range(n):
            # 1ª Prioridade: Centro exato
            if i == centro and j == centro:
                linha.append("4")
            # 2ª Prioridade: Quadrado interno
            elif borda_quadrado <= i < n - borda_quadrado and borda_quadrado <= j < n - borda_quadrado:
                linha.append("1")
            # 3ª Prioridade: Diagonal principal
            elif i == j:
                linha.append("2")
            # 4ª Prioridade: Diagonal secundária
            elif i + j == n - 1:
                linha.append("3")
            # Fundo
            else:
                linha.append("0")

        print("".join(linha))
    print()
