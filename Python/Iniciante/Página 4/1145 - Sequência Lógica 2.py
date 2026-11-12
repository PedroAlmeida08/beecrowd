entrada = list(map(int, input().split()))
for i in range(1, entrada[1]+1):
    if i % entrada[0] == 0:
        print(i)
    else:
        print(i, end=" ")
