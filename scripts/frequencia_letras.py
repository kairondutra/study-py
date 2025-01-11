import string

def frequencia_letra():
    texto = input("Escreva a palavra/texto: ")
    texto = texto.replace(" ", "").lower()
    texto = texto.translate(str.maketrans("", "", string.punctuation))
    
    # Inicializar um dicionário para as frequências
    frequencias = {}
    
    # Contar a frequência de cada letra
    for letra in texto:
        if letra.isalpha():  # Certifique-se de contar apenas letras
            if letra in frequencias:
                frequencias[letra] += 1
            else:
                frequencias[letra] = 1

    # Exibir o resultado em ordem alfabética
    for letra in sorted(frequencias.keys()):
        print(f"{letra}: {frequencias[letra]}")

frequencia_letra()