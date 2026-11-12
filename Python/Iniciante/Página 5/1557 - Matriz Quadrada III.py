while True:
    n = int(input())
    
    if n == 0:
        break
        
    # 1. Encontra o maior valor da matriz (canto inferior direito)
    maior_valor = 2 ** ((n - 1) + (n - 1))
    
    # 2. Descobre quantos dígitos esse número tem
    tamanho = len(str(maior_valor))
    
    for i in range(n):
        linha = []
        for j in range(n):
            valor = 2 ** (i + j)
            linha.append(f"{valor:>{tamanho}}")
            
        print(" ".join(linha))
        
    print()