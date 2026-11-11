tam = int(input())
pesos = [2, 3, 5]
for i in range(tam):
    media = 0
    nums = list(map(float, input().split()))
    for num, peso in zip(nums, pesos):
        media += num * peso
    media /= sum(pesos)
    print(f"{media:.1f}")
