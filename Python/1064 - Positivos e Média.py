v_media = []
for i in range(6):
    n = float(input())
    if n > 0:
        v_media.append(n)

media = 0
for n in v_media:
    media += n

media /= len(v_media)

print(f"{len(v_media)} valores positivos")
print(f"{media:.1f}")
