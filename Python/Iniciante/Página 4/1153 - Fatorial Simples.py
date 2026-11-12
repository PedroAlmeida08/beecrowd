n = int(input())
fatorial = n
if n == 0 or n == 1:
    fatorial = 1
else:
    for i in range(1, n):
        fatorial *= (n - i)
print(fatorial)