# -*- coding: utf-8 -*-

produtos = [
    {"codigo": 1, "nome": "Cachorro Quente", "preco": 4.00},
    {"codigo": 2, "nome": "X-Salada", "preco": 4.50},
    {"codigo": 3, "nome": "X-Bacon", "preco": 5.00},
    {"codigo": 4, "nome": "Torrada simples", "preco": 2.00},
    {"codigo": 5, "nome": "Refrigerante", "preco": 1.50}
]

entrada = list(map(int, input().split()))
total = 0
for produto in produtos:
    if entrada[0] == produto['codigo']:
        total += entrada[1] * produto['preco']

print(f'Total: R$ {total:.2f}')