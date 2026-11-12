n = int(input())
fibonacci = []
for i in range(n):
    if i == 0 or i == 1:
        fibonacci.append(i)
    else:
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

print(*fibonacci)