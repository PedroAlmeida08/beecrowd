TAMANHO = 12


def soma_coluna(matriz: list[list[float]], coluna: int, tam: int) -> float:
    soma = 0
    for i in range(tam):
        soma += matriz[i][coluna]
    return soma


coluna_alvo = int(input())
operacao = input()

matriz = []

for i in range(TAMANHO):
    linha = []
    for j in range(TAMANHO):
        valor = float(input())
        linha.append(valor)

    matriz.append(linha)

if operacao == 'S':
    resultado = soma_coluna(matriz, coluna_alvo, TAMANHO)
elif operacao == 'M':
    resultado = soma_coluna(matriz, coluna_alvo, TAMANHO) / TAMANHO

print(f"{resultado:.1f}")
