opt = 1
while opt == 1:
    ct, soma = 0, 0
    while ct < 2:
        n = float(input())
        if 0 <= n <= 10:
            ct += 1
            soma += n
        else:
            print("nota invalida")
    print(f"media = {soma/ct:.2f}")
    print("novo calculo (1-sim 2-nao)")
    opt = int(input())
    while opt != 1 and opt != 2:
        print("novo calculo (1-sim 2-nao)")
        opt = int(input())
