n = list(map(int, input().split()))
d1 = n[0]
d2 = n[1]
d3 = n[2]

# Se a temperatura desceu
if d1 > d2:
    # Figura 1
    if d2 <= d3:
        feliz = 1
    else:
        # Figura 5
        if abs(d2-d1) > abs(d3-d2):
            feliz = 1
        # Figura 6
        else:
            feliz = 0
# Se a temperatura subiu
elif d1 < d2:
    # Figura 2
    if d2 >= d3:
        feliz = 0
    else:
        # Figura 3
        if abs(d2-d1) > abs(d3-d2):
            feliz = 0
        else:
            # Figura 4
            feliz = 1
# Temperatura se manteve
else:
    # Figura 7
    if d2 < d3:
        feliz = 1
    # Figura 8
    else:
        feliz = 0

if feliz == 1:
    print(":)")
else:
    print(":(")