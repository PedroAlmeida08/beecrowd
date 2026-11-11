entrada = list(map(int, input().split()))
while entrada[0] != entrada[1]:
    if entrada[0] < entrada[1]:
        print("Crescente")
    else:
        print("Decrescente")
    entrada = list(map(int, input().split()))
