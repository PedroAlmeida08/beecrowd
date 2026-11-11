valores = list(map(float, input().split()))
delta = valores[1]**2 - 4 * valores[0] * valores[2]
if delta < 0 or valores[0] <= 0:
    print('Impossivel calcular')
else:
    r1 = ((-1)*valores[1] + delta ** (1/2)) / (2 * valores[0])
    r2 = ((-1)*valores[1] - delta ** (1/2)) / (2 * valores[0])
    print(f'R1 = {r1:.5f}\nR2 = {r2:.5f}')
