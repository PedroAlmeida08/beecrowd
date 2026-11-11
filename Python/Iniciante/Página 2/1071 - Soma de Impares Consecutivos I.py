intervalo = sorted([int(input()), int(input())])
soma = 0

for i in range(intervalo[0] + 1, intervalo[1]):
    if i % 2 != 0:
        soma += i

print(soma)
