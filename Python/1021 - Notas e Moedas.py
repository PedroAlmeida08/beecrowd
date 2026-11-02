valor = float(input())
centavos = int(round(valor * 100))

notas = [100, 50, 20, 10, 5, 2]
moedas = [100, 50, 25, 10, 5, 1]

print("NOTAS:")
for nota in notas:
    valor_nota = nota * 100
    qtd = centavos // valor_nota
    centavos %= valor_nota
    print(f"{qtd} nota(s) de R$ {nota}.00")

print("MOEDAS:")
for moeda in moedas:
    qtd = centavos // moeda
    centavos %= moeda
    print(f"{qtd} moeda(s) de R$ {moeda / 100:.2f}")
