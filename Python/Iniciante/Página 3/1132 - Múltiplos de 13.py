ini = int(input())
fim = int(input())
lista = sorted([ini, fim])
soma = 0
for i in range(lista[0], lista[1]+1):
    if i % 13 != 0:
        soma += i
print(soma)
