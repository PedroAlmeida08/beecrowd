soma = []
while True:
    idade = float(input())
    if idade < 0:
        break
    else:
        soma.append(idade)
print(f"{sum(soma)/len(soma):.2f}")