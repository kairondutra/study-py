import string

def palindromo():
    texto = input("Escreva uma palavra/texto para verificação: ")

    texto = texto.replace(" ", "").lower()
    texto = texto.translate(str.maketrans("", "", string.punctuation))

    if texto == texto[::-1]:
        return print("É palindromo!")
    else:
        return print("Não é um palindromo!")

palindromo()