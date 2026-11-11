coordenadas = list(map(int, input().split()))
while coordenadas[0] != 0 and coordenadas[1] != 0:
    if coordenadas[0] > 0 and coordenadas[1] > 0:
        print('primeiro')
    elif coordenadas[0] < 0 and coordenadas[1] > 0:
        print('segundo')
    elif coordenadas[0] < 0 and coordenadas[1] < 0:
        print('terceiro')
    elif coordenadas[0] > 0 and coordenadas[1] < 0:
        print('quarto')
    coordenadas = list(map(int, input().split()))
