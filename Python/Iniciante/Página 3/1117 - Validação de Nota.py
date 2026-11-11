ct, soma = 0, 0
while ct < 2:
    n = float(input())
    if 0 <= n <= 10:
        ct += 1
        soma += n
    else:
        print("nota invalida")
print(f"media = {soma/ct}")
