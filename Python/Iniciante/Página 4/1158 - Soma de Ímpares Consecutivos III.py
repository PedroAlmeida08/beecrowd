tam = int(input())
for i in range(tam):
    entrada = list(map(int, input().split()))
    soma, ct = 0, 0
    i = entrada[0]
    while ct < entrada[1]:
        if i % 2 != 0:
            soma += i
            i += 2
            ct += 1
        else:
            i += 1
    print(soma)