tam = int(input())
for i in range(tam):
    n = int(input())
    if n == 0:
        print("NULL")
    elif n % 2 == 0 and n > 0:
        print("EVEN POSITIVE")
    elif n % 2 == 0 and n < 0:
        print("EVEN NEGATIVE")
    elif n > 0:
        print("ODD POSITIVE")
    else:
        print("ODD NEGATIVE")
