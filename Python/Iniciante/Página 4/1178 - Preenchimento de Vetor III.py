n = float(input())
print(f"N[0] = {n:.4f}")
j = n/2
for i in range(1, 100):
    print(f"N[{i}] = {j:.4f}")
    j /= 2