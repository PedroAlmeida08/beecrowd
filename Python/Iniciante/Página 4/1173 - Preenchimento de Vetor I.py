n = int(input())
for i in range(10):
    if i == 0:
        print(f"N[{i}] = {n}")
    else:
        n *= 2
        print(f"N[{i}] = {n}")