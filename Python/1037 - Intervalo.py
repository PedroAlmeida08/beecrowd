val = float(input())

if val > 100 or val < 0:
    print('Fora de intervalo')
else:
    if val > 75:
        print('Intervalo (75,100]')
    elif val > 50:
        print('Intervalo (50,75]')
    elif val > 25:
        print('Intervalo (25,50]')
    elif val >= 0:
        print('Intervalo [0,25]')
