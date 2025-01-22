def fatorial():
    numero = int(input("Escreva o número a ser fatorado: "))
    
    if numero < 0:
        print("Erro: O fatorial não é definido para números negativos.")
        return None  # Retorna None em caso de erro
    else:
        auxiliar = numero
        resultado = 1
        while auxiliar > 0:
            resultado *= auxiliar
            auxiliar -= 1
        return resultado

resultado = fatorial()
if resultado is not None:
    print("Resultado:", resultado)

