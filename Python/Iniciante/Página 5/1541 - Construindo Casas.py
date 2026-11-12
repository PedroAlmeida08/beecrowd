while True:
    n = list(map(int, input().split()))
    
    if n[0] == 0:
        break
        
    area = n[0] * n[1]
    percent = (area * 100) / n[2]
    lado = int(percent ** 0.5)
    print(lado)