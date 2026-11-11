qtd, inter, gremio, empate = 0, 0, 0, 0
opt = 1
while opt == 1:
    partida = list(map(int, input().split()))
    qtd += 1
    if partida[0] > partida[1]:
        inter += 1
    elif partida[0] < partida[1]:
        gremio += 1
    else:
        empate += 1

    print("Novo grenal (1-sim 2-nao)")
    opt = int(input())
    while opt != 1 and opt != 2:
        print("Novo grenal (1-sim 2-nao)")
        opt = int(input())

if inter > gremio:
    vencedor = "Inter"
elif inter < gremio:
    vencedor = "Gremio"
else:
    vencedor = "Nao houve vencedor"

print(f"{qtd} grenais")
print(f"Inter:{inter}")
print(f"Gremio:{gremio}")
print(f"Empates:{empate}")
print(f"{vencedor} venceu mais")
