def contador_vogais_consoantes():
    texto = input("Escreva uma palavra ou frase: ")
    
    vogais = 0
    consoantes = 0
    for letra in texto:
        if letra.lower() in "aeiou":  # Verificar se a letra é uma vogal
            vogais += 1
        elif letra.isalpha():  # Verifica se é uma letra (ignora números e pontuações)
            consoantes += 1
    
    print(f"A palavra/frase tem {vogais} vogais e {consoantes} consoantes.")

contador_vogais_consoantes()
