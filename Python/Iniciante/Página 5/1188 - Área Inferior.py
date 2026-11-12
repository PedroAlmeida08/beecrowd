TAMANHO = 12

def soma_da_area_inferior(matriz: list[list[float]], tam: int) -> float:
    soma = 0
    for i in range(tam//2, tam):
        soma += sum(matriz[i][tam-i:i])
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
    resultado = soma_da_area_inferior(matriz, TAMANHO)
elif operacao == 'M':
    qtd_elementos = ((TAMANHO * TAMANHO) // 4) - (TAMANHO // 2)
    resultado = soma_da_area_inferior(matriz, TAMANHO) / qtd_elementos

print(f"{resultado:.1f}")