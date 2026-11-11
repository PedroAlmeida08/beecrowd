salario = float(input())
if salario <= 400:
    bonus = salario * 0.15
    percentual = 15
elif salario <= 800:
    bonus = salario * 0.12
    percentual = 12
elif salario <= 1200:
    bonus = salario * 0.1
    percentual = 10
elif salario <= 2000:
    bonus = salario * 0.07
    percentual = 7
else:
    bonus = salario * 0.04
    percentual = 4

print(f'Novo salario: {salario + bonus:.2f}')
print(f'Reajuste ganho: {bonus:.2f}')
print(f'Em percentual: {percentual} %')
