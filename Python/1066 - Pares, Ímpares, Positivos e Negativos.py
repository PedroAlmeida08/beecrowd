ct_par, ct_impar, ct_pos, ct_neg = 0, 0, 0, 0
for i in range(5):
    n = float(input())
    if n % 2 == 0:
        ct_par += 1
    else:
        ct_impar += 1
    if n > 0:
        ct_pos += 1
    elif n < 0:
        ct_neg += 1

print(f"{ct_par} valor(es) par(es)")
print(f"{ct_impar} valor(es) impar(es)")
print(f"{ct_pos} valor(es) positivo(s)")
print(f"{ct_neg} valor(es) negativo(s)")
