qtd = int(input())
qtd_coelhos, qtd_ratos, qtd_sapos = 0, 0, 0
for i in range(qtd):
    qtd, tipo = input().split()
    qtd = int(qtd)
    if tipo == "C":
        qtd_coelhos += qtd
    elif tipo == "R":
        qtd_ratos += qtd
    else:
        qtd_sapos += qtd

total = qtd_coelhos + qtd_ratos + qtd_sapos
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {qtd_coelhos}")
print(f"Total de ratos: {qtd_ratos}")
print(f"Total de sapos: {qtd_sapos}")
print(f"Percentual de coelhos: {(qtd_coelhos/total)*100:.2f} %")
print(f"Percentual de ratos: {(qtd_ratos/total)*100:.2f} %")
print(f"Percentual de sapos: {(qtd_sapos/total)*100:.2f} %")
