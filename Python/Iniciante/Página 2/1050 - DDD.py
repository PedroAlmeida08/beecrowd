codigos = [
    {"ddd": 61, "destino": "Brasilia"},
    {"ddd": 71, "destino": "Salvador"},
    {"ddd": 11, "destino": "Sao Paulo"},
    {"ddd": 21, "destino": "Rio de Janeiro"},
    {"ddd": 32, "destino": "Juiz de Fora"},
    {"ddd": 19, "destino": "Campinas"},
    {"ddd": 27, "destino": "Vitoria"},
    {"ddd": 31, "destino": "Belo Horizonte"}
]

codigo = int(input())
destino = "DDD nao cadastrado"
for cod in codigos:
    if cod["ddd"] == codigo:
        destino = cod["destino"]

print(destino)
