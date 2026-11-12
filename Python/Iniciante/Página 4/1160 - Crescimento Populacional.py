t = int(input())

for i in range(t):
    valores = input().split()
    pa = int(valores[0])
    pb = int(valores[1])
    g1 = float(valores[2])
    g2 = float(valores[3])
    
    anos = 0
    
    while pa <= pb:
        pa += int(pa * (g1 / 100))
        pb += int(pb * (g2 / 100))
        anos += 1
        
        if anos > 100:
            break
            
    if anos > 100:
        print("Mais de 1 seculo.")
    else:
        print(f"{anos} anos.")