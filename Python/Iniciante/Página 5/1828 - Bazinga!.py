n = int(input())
for i in range(1, n+1):
    sheldon, raj = input().split()
    if sheldon == raj:
        print(f"Caso #{i}: De novo!")
    else:
        if (sheldon == "tesoura" and raj == "papel") or  (sheldon == "papel" and raj == "pedra") or (sheldon == "pedra" and raj == "lagarto") or (sheldon == "lagarto" and raj == "Spock") or (sheldon == "Spock" and raj == "tesoura") or (sheldon == "tesoura" and raj == "lagarto") or (sheldon == "lagarto" and raj == "papel") or (sheldon == "papel" and raj == "Spock") or (sheldon == "Spock" and raj == "pedra") or (sheldon == "pedra" and raj == "tesoura"):
            print(f"Caso #{i}: Bazinga!")
        else:
            print(f"Caso #{i}: Raj trapaceou!")