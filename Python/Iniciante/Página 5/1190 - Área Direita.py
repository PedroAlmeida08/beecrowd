TAMANHO = 12

def soma_da_area_direita(matriz: list[list[float]], tam: int) -> float:
    soma = 0
    for i in range(1, tam - 1):
        if i < tam // 2:
            soma += sum(matriz[i][tam-i:])
        else:
            soma += sum(matriz[i][i+1:])
        
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
    resultado = soma_da_area_direita(matriz, TAMANHO)
elif operacao == 'M':
    qtd_elementos = ((TAMANHO * TAMANHO) // 4) - (TAMANHO // 2)
    resultado = soma_da_area_direita(matriz, TAMANHO) / qtd_elementos

print(f"{resultado:.1f}")