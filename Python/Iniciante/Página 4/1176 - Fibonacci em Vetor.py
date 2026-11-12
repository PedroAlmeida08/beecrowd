n = int(input())

entradas = []
for i in range(n):
    entradas.append(int(input()))

fibonacci = []
for i in range(max(entradas)+1):
    if i == 0 or i == 1:
        fibonacci.append(i)
    else:
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

for entrada in entradas:
    print(f"Fib({entrada}) = {fibonacci[entrada]}")