# -*- coding: utf-8 -*-

def forma_triangulo(a: float, b: float, c: float) -> bool:
    if a+b > c and a+c > b and b+c > a:
        return True
    else:
        return False


lista = list(map(float, input().split()))
a = lista[0]
b = lista[1]
c = lista[2]
if forma_triangulo(a, b, c):
    print(f'Perimetro = {a+b+c:.1f}')
else:
    print(f'Area = {((a+b)*c)/2:.1f}')
