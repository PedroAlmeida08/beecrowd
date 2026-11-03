# -*- coding: utf-8 -*-

def calcula_media(notas: list[float], pesos: list[int]) -> float:
    media = 0
    for i in range(len(notas)):
        media += notas[i] * pesos[i]
    media /= sum(pesos)
    return media


notas = list(map(float, input().split()))
pesos = [2, 3, 4, 1]
media = calcula_media(notas, pesos)

print(f'Media: {media:.1f}')
if media >= 7:
    print('Aluno aprovado.')
elif media < 5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    nota_exame = float(input())
    print(f'Nota do exame: {nota_exame:.1f}')
    media = (media + nota_exame)/2
    print(f"Aluno {'aprovado' if media >= 5.0 else 'reprovado'}.")
    print(f'Media final: {media:.1f}')
