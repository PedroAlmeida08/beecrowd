entrada = list(map(int, input().split()))
while entrada[0] > 0 and entrada[1] > 0:
    seq = sorted(entrada)
    soma = 0
    for i in range(seq[0], seq[1]+1):
        soma += i
        print(i, end=" ")
    print(f"Sum={soma}")
    entrada = list(map(int, input().split()))
