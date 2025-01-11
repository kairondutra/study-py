
def calculadora_de_dois_valores():
    
    print("Calculadora Simples")
    print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")
    operacao = int(input("Envie o número referente à Operação: "))
    numero1 = int(input("Informe o primeiro número: "))
    numero2 = int(input("Informe o segundo número: "))

    if operacao == 1:
        resultado = numero1 + numero2
        return print("= ",resultado)
    elif operacao == 2:
        resultado = numero1 - numero2
        return print("= ",resultado)
    elif operacao == 3:
        resultado = numero1 * numero2
        return print("= ",resultado)
    elif operacao == 4:
        resultado = numero1 / numero2
        return print("= ",resultado)
    else:
        return print("Operação inválida")
        
calculadora_de_dois_valores()
