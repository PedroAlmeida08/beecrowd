while True:
    x = int(input())
    soma, ct = 0, 0
    i = x
    if x == 0:
        break
    else:
        while ct < 5:
            if i % 2 == 0:
                soma += i
                i += 2
                ct += 1
            else:
                i += 1
        print(soma)