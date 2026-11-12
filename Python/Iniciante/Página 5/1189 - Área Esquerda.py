TAMANHO = 12

def soma_da_area_esquerda(matriz: list[list[float]], tam: int) -> float:
    soma = 0
    for i in range(1, tam - 1):
        if i < tam // 2:
            soma += sum(matriz[i][:i])
        else:
            soma += sum(matriz[i][:tam - 1 - i])
        
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
    resultado = soma_da_area_esquerda(matriz, TAMANHO)
elif operacao == 'M':
    qtd_elementos = ((TAMANHO * TAMANHO) // 4) - (TAMANHO // 2)
    resultado = soma_da_area_esquerda(matriz, TAMANHO) / qtd_elementos

print(f"{resultado:.1f}")