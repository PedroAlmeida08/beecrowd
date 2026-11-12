tam = int(input())

for i in range(tam):
    x = int(input())
    ct = 0
    for i in range(1, x+1):
        if x % i == 0:
            ct += 1
    if ct == 2:
        print(f"{x} eh primo")
    else:
        print(f"{x} nao eh primo")