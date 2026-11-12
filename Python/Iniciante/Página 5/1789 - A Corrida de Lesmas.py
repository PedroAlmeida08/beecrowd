import sys

for linha in sys.stdin:
    n = int(linha)

    veloz = max(list(map(int, input().split())))

    if veloz < 10:
        grupo = 1
    elif veloz < 20:
        grupo = 2
    else:
        grupo = 3

    print(grupo)