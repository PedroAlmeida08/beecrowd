opt = int(input())
alcool, gasolina, diesel = 0, 0, 0
while opt != 4:
    match opt:
        case 1:
            alcool += 1
        case 2:
            gasolina += 1
        case 3:
            diesel += 1
    opt = int(input())

print("MUITO OBRIGADO")
print(f"Alcool: {alcool}")
print(f"Gasolina: {gasolina}")
print(f"Diesel: {diesel}")
