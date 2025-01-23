from itertools import permutations

# Entrada do usuário
texto = input("Digite uma palavra ou texto para gerar anagramas: ").replace(" ", "")

# Gerar anagramas
anagramas = set("".join(p) for p in permutations(texto))

# Exibir resultados
print("Anagramas encontrados:")
print(", ".join(anagramas))
