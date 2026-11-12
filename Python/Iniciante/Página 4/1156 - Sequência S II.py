s, j = 1, 1
for i in range(3, 40, 2):
    s += (i/(2**j))
    j += 1
print(f"{s:.2f}")