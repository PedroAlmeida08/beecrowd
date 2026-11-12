def imprimir_e_limpar(lista, nome):
    for i, valor in enumerate(lista):
        print(f"{nome}[{i}] = {valor}")
    lista.clear()

par = []
impar = []

for _ in range(15):
    n = int(input())
    
    if n % 2 == 0:
        par.append(n)
        if len(par) == 5:
            imprimir_e_limpar(par, "par")
    else:
        impar.append(n)
        if len(impar) == 5:
            imprimir_e_limpar(impar, "impar")

imprimir_e_limpar(impar, "impar")
imprimir_e_limpar(par, "par")