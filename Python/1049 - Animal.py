esqueleto = input()
classe = input()
alimentacao = input()

if esqueleto == 'vertebrado':
    if classe == 'ave':
        if alimentacao == 'carnivoro':
            animal = 'aguia'
        else:
            animal = 'pomba'
    else:
        if alimentacao == 'onivoro':
            animal = 'homem'
        else:
            animal = 'vaca'
else:
    if classe == 'inseto':
        if alimentacao == 'hematofago':
            animal = 'pulga'
        else:
            animal = 'lagarta'
    else:
        if alimentacao == 'hematofago':
            animal = 'sanguessuga'
        else:
            animal = 'minhoca'

print(animal)
