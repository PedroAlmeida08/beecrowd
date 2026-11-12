import sys

for linha in sys.stdin:
    n = int(linha)

    if n == 0:
        print("vai ter copa!")
    else:
        print("vai ter duas!")
