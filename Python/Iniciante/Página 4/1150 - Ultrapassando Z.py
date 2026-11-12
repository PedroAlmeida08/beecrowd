x = int(input())
z = x-1
while z <= x:
    z = int(input())
soma, ct, i = 0, 0, x
while True:
    if soma > z:
        break
    else:
        soma+= i
        i += 1
        ct += 1

print(ct)