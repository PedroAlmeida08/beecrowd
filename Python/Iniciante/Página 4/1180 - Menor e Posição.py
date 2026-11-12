n = int(input())
nums = list(map(int, input().split()))
menor = min(nums)
for i in range(n):
    if nums[i] == menor:
        print(f"Menor valor: {menor}")
        print(f"Posicao: {i}")