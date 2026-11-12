TAMANHO = 12

def soma_acima_da_diagonal_secundaria(matriz: list[list[float]], tam: int) -> float:
    soma = 0
    for i in range(tam):
        for j in range(tam - i - 1):
            soma += matriz[i][j]
    return soma

operacao = input()

matriz = []

for i in range(TAMANHO):
    linha = []
    for j in range(TAMANHO):
        valor = float(input())
        linha.append(valor)
    
    matriz.append(linha)

if operacao == 'S':
    resultado = soma_acima_da_diagonal_secundaria(matriz, TAMANHO)
elif operacao == 'M':
    qtd_elementos = ((TAMANHO * TAMANHO) - TAMANHO) // 2
    resultado = soma_acima_da_diagonal_secundaria(matriz, TAMANHO) / qtd_elementos

print(f"{resultado:.1f}")