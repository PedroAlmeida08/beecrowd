n = list(map(int, input().split()))
r = n[0] % abs(n[1])
q = (n[0] - r) // n[1]
print(f"{q} {r}")