ct = 0
soma = 0

while ct < 3:
    entrada = input()
    
    if entrada == "caw caw":
        print(soma)
        soma = 0
        ct += 1
    else:
        if entrada[0] == "*": soma += 2**2
        if entrada[1] == "*": soma += 2**1
        if entrada[2] == "*": soma += 2**0