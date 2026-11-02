total = 0
for i in range(2):
    codigo, n, valor = input().split()
    n = int(n)
    valor = float(valor)
    total += (n * valor)

print(f'VALOR A PAGAR: R$ {total:.2f}')
