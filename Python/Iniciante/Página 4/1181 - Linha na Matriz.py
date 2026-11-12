TAMANHO = 12

linha_alvo = int(input())
operacao = input()

matriz = []

for i in range(TAMANHO):
    linha = []
    for j in range(TAMANHO):
        valor = float(input())
        linha.append(valor)

    matriz.append(linha)

linha_escolhida = matriz[linha_alvo]

if operacao == 'S':
    resultado = sum(linha_escolhida)
elif operacao == 'M':
    resultado = sum(linha_escolhida) / TAMANHO

print(f"{resultado:.1f}")
