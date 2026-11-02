def area_triangulo(A, C):
    return (A*C)/2


def area_circulo(C):
    return 3.14159 * C**2


def area_trapezio(A, B, C):
    return ((A+B)*C)/2


def area_quadrado(B):
    return B**2


def area_retangulo(A, B):
    return A*B


A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

print(f'TRIANGULO: {area_triangulo(A, C):.3f}')
print(f'CIRCULO: {area_circulo(C):.3f}')
print(f'TRAPEZIO: {area_trapezio(A, B, C):.3f}')
print(f'QUADRADO: {area_quadrado(B):.3f}')
print(f'RETANGULO: {area_retangulo(A, B):.3f}')
