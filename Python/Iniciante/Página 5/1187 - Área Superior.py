TAMANHO = 12

def soma_da_area_superior(matriz: list[list[float]], tam: int) -> float:
    soma = 0
    for i in range(tam//2):
        soma += sum(matriz[i][i+1:tam-i-1])
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
    resultado = soma_da_area_superior(matriz, TAMANHO)
elif operacao == 'M':
    qtd_elementos = ((TAMANHO * TAMANHO) // 4) - (TAMANHO // 2)
    resultado = soma_da_area_superior(matriz, TAMANHO) / qtd_elementos

print(f"{resultado:.1f}")