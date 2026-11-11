tam = int(input())
for i in range(tam):
    nums = list(map(float, input().split()))
    if nums[1] == 0:
        print("divisao impossivel")
    else:
        print(f"{nums[0]/nums[1]:.1f}")
