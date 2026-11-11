def volume_esfera(raio: float) -> float:
    return (4.0/3) * 3.14159 * raio**3


raio = float(input())
print(f'VOLUME = {volume_esfera(raio):.3f}')
