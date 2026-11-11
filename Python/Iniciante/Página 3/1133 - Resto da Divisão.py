ini = int(input())
fim = int(input())
lista = sorted([ini, fim])
for i in range(lista[0]+1, lista[1]):
    if i % 5 == 2 or i % 5 == 3:
        print(i)
