import os

def menu():
    """
    Mostra o menu principal da ferramenta.
    """
    print("\nEscolha uma funcionalidade:")
    print("1. Algoritmo de Euclides (MDC)")
    print("2. Calculadora simples")
    print("3. Conversor de Temperaturas")
    print("4. Sequencia Fibonacci")
    print("5. Mínimo Múltiplo Comum")
    print("6. Índice de Massa Corporal")
    print("7. Calcular Hipotenusa")
    print("8. Sair")
    try:
        return int(input("Digite o número da sua escolha: "))
    except ValueError:
        return 0  # Retorna uma escolha inválida em caso de erro

def calcular_mdc(a, b):
    """
    Calcula o Máximo Divisor Comum (MDC) de dois números inteiros.
    """
    if a < 0 or b < 0:
        raise ValueError("Os valores não podem ser negativos!")
    if a < b:
        a, b = b, a
    while b != 0:
        resto = a % b
        a, b = b, resto
    return a

def calculadora_simples():
    """
    Calcula operações simples entre duas operandos
    """
    while True:
        print("\nCalculadora Simples:")
        print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Voltar ao Menu Principal")
        try:
            operacao = int(input("Informe uma operação (1-5): "))
        except ValueError:
            print("Por favor, informe um valor válido.")
            continue

        if operacao == 5:
            break

        if operacao not in [1, 2, 3, 4]:
            print("Operação inválida. Escolha uma das opções (1-5).")
            continue

        try:
            numero1 = float(input("Informe o primeiro valor: "))
            numero2 = float(input("Informe o segundo valor: "))
        except ValueError:
            print("Por favor, insira números válidos.")
            continue

        if operacao == 1:
            print(f"Resultado da soma: {numero1 + numero2}")
        elif operacao == 2:
            print(f"Resultado da subtração: {numero1 - numero2}")
        elif operacao == 3:
            print(f"Resultado da multiplicação: {numero1 * numero2}")
        elif operacao == 4:
            if numero2 == 0:
                print("Erro: Divisão por zero não é permitida.")
            else:
                print(f"Resultado da divisão: {numero1 / numero2}")

def conversor_de_temperatura():
    """
    Calcula o valor correspondente para a outra temperatura.
    """
    while True:
        print("=== Conversor de Temperaturas ===".center(40, "="))
        print("1. Celsius para Fahrenheit")
        print("2. Fahrenheit para Celsius")
        print("3. Celsius para Kelvin")
        print("4. Kelvin para Celsius")
        print("5. Fahrenheit para Kelvin")
        print("6. Kelvin para Fahrenheit")
        print("7. Sair")
        try:
            opcao = int(input("Escolha uma opção (1-7): "))
        except ValueError:
            print("Por favor, informe um valor válido.")
            continue

        if opcao == 7:
            break

        if opcao not in range(1, 7):
            print("Escolha uma opção válida entre 1 e 7!")
            continue

        try:
            mensagens = {
                1: "Insira o valor em Celsius: ",
                2: "Insira o valor em Fahrenheit: ",
                3: "Insira o valor em Celsius: ",
                4: "Insira o valor em Kelvin: ",
                5: "Insira o valor em Fahrenheit: ",
                6: "Insira o valor em Kelvin: ",
            }
            user = float(input(mensagens[opcao]))
        except ValueError:
            print("Por favor, insira números válidos.")
            continue

        if opcao in [3, 4, 6] and user < 0:
            print("O valor em Kelvin não pode ser negativo!")
            continue

        if opcao == 1:
            resultado = (user * 9 / 5) + 32
        elif opcao == 2:
            resultado = (user - 32) / 1.8
        elif opcao == 3:
            resultado = user + 273.15
        elif opcao == 4:
            resultado = user - 273.15
        elif opcao == 5:
            resultado = ((user + 459.67) * 5) / 9
        elif opcao == 6:
            resultado = (user * 1.8) - 459.67

        print(f"Resultado: {resultado:.2f}")

def fibonacci(n):
    """
    Lista a sequencia fibonacci de 0 a n.
    """
    if n <= 0:
        return []
    fib = [0, 1]
    for _ in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib[:n]

def calcular_imc(peso, altura):
    """
    Calcula o índice de massa corporal.
    """
    return peso / (altura ** 2)

def classificar_imc(imc):
    """
    Classifica de acordo com o valor do imc.
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade Grau I"
    elif 35 <= imc < 40:
        return "Obesidade Grau II"
    else:
        return "Obesidade Grau III"

def mmc(a, b):
    """
    Calcula o Minimo Multiplo Comum (MMC) de dois números inteiros.
    """
    maior = max(a, b)
    while True:
        if maior % a == 0 and maior % b == 0:
            return maior
        maior += 1

def pythagorean_theorem(a,b):
    c = (a**2+ b**2)**0.5
    return c

# Mapeando as opções para as funções correspondentes
opcoes = {
    1: lambda: print(f"Resultado do MDC: {calcular_mdc(int(input('A: ')), int(input('B: ')))}"),
    2: calculadora_simples,
    3: conversor_de_temperatura,
    4: lambda: print(f"Sequência Fibonacci: {fibonacci(int(input('Quantidade de termos: ')))}"),
    5: lambda: print(f"MMC: {mmc(int(input('A: ')), int(input('B: ')))}"),
    6: lambda: print(f"IMC: {classificar_imc(calcular_imc(float(input('Peso: ')), float(input('Altura: '))))}"),
    7: lambda: print(f"Hipotenusa é igual a {pythagorean_theorem(float(input("Informe o cateto a: ")),float(input("Informe o cateto b: ")))}")
}

# Programa principal
while True:
    escolha = menu()
    if escolha == 8:
        print("Saindo do programa...")
        break
    elif escolha in opcoes:
        opcoes[escolha]()
    else:
        print("Opção inválida. Tente novamente!")
