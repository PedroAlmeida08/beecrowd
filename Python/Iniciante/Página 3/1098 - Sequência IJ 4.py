for i in range(11):
    valor_i = i / 5

    for j in range(1, 4):
        valor_j = valor_i + j

        if i % 5 == 0:
            print(f"I={int(valor_i)} J={int(valor_j)}")
        else:
            print(f"I={valor_i:.1f} J={valor_j:.1f}")
