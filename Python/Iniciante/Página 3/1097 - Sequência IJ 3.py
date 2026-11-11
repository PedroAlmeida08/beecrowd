i = 1
j = [7, 6, 5]
while i <= 9:
    for e in j:
        print(f"I={i} J={e}")
    i += 2
    j = [x + 2 for x in j]
