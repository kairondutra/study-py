import random

palavras = ["gengar", "kirlia", "raichu", "kadabra", "rayquaza"]
palavra_secreta = random.choice(palavras)
#print(palavra_secreta)

progresso = ["_"] * len(palavra_secreta)
tentativas = 6

while tentativas > 0:
    print("\nProgresso: ", " ".join(progresso))
    print(f"Tentativas restantes: {tentativas}")

    palpite = input("Digite uma letra ou tente adivinhar a palavra inteira: ").lower()

    if len(palpite) > 1:
        if palpite == palavra_secreta:
            print(f"\nParabéns! Você acertou a palavra: {palavra_secreta}")
            break
        else:
            tentativas -= 2
            print("Palavra incorreta! Você perdeu uma tentativa.")
            continue

    if len(palpite) != 1 or not palpite.isalpha():
        print("Por favor, digite apenas uma letra válida ou tente adivinhar a palavra inteira.")
        continue

    if palpite in palavra_secreta:
        for i, letra in enumerate(palavra_secreta):
            if letra == palpite:
                progresso[i] = letra
        print("Boa! Você acertou uma letra.")
    else:
        tentativas -= 1
        print("Ops! Letra errada.")

    if "_" not in progresso:
        print(f"\nParabéns! Você acertou a palavra: {palavra_secreta}")
        break
else:
    print(f"\nVocê perdeu! A palavra era: {palavra_secreta}")
