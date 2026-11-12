vetor = []
for i in range(20):
    vetor.append(int(input()))

i = 0
j = len(vetor) - 1

while i < j:
    aux = vetor[i]
    vetor[i] = vetor[j]
    vetor[j] = aux
    i += 1
    j -= 1

for k in range(len(vetor)):
    print(f"N[{k}] = {vetor[k]}")