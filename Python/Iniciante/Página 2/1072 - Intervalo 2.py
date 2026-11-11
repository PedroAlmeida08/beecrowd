tam = int(input())
ct_in, ct_out = 0, 0
for i in range(tam):
    n = int(input())
    if 10 <= n <= 20:
        ct_in += 1
    else:
        ct_out += 1
print(f"{ct_in} in")
print(f"{ct_out} out")
