import os

def conversor_de_temperatura():
    
    while True:
        # 1. Menu de opções
        print("=== Conversor de Temperaturas ===")
        print("1. Celsius para Fahrenheit")
        print("2. Fahrenheit para Celsius")
        print("3. Celsius para Kelvin")
        print("4. Kelvin para Celsius")
        print("5. Fahrenheit para Kelvin")
        print("6. Kelvin para Fahrenheit")
        print("7. Sair")

        try:
            # Entrada do usuário
            opcao = int(input("Escolha uma opção (1-7): "))

            # 2. tratamento da escolha
        except ValueError: 
            # Se o usuário inserir um valor inválido, exibe uma mensagem de erro e reinicia o loop
            print("Por favor, informe um valor válido.")
            input("Pressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        
        # Verifica se o usuário escolheu sair
        if opcao == 7:
            print("Encerrando...")
            break
        
        # Verifica se a operação escolhida é válida (1-7)
        if opcao not in [1, 2, 3, 4, 5, 6, 7]:
            print("Operação inválida. Escolha uma das opções (1-7).")
            input("Pressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        
        # Solicita os dois valores para a operação
        try:
            if opcao == 1:
                user = float(input("Insira o valor em Celsius: "))
            elif opcao == 2:
                user = float(input("Insira o valor em Fahrenheit: "))
            elif opcao == 3:
                user = float(input("Insira o valor em Celsius: "))
            elif opcao == 4:
                user = float(input("Insira o valor em Kelvin: "))
            elif opcao == 5:
                user = float(input("Insira o valor em Fahrenheit: "))
            elif opcao == 6:
                user = float(input("Insira o valor em Kelvin: "))
            

        except ValueError:
            # Se o usuário inserir um valor inválido, exibe uma mensagem de erro e reinicia o loop
            print("Por favor, insira números válidos.")
            input("Pressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
            
        # Executa a operação escolhida
        if opcao == 1:
            # Celsius para Fahrenheit
            resultado = float((user * 9/5) + 32 )
            print(f"{user}°C = {resultado:.2f}°F\n")
        elif opcao == 2:
            # Fahrenheit para Celsius
            resultado = float((user - 32) / 1.8)
            print(f"{user}°F = {resultado:.2f}°C\n")
        elif opcao == 3:
            # Celsius para Kelvin
            resultado = float(user + 273.15)
            print(f"{user}°C = {resultado:.2f}°K\n")
        elif opcao == 4:
            # Kelvin para Celcius
            resultado = float(user - 273.15)
            print(f"{user}°K = {resultado:.2f}°C\n")
        elif opcao == 5: 
            # Fahrenheit para Kelvin 
            resultado = float(((user + 459.67) * 5)/9)
            print(f"{user}°F = {resultado:.2f}°K\n")
        elif opcao == 6:
            # Kelvin para Fahrenheit
            resultado = float((user * 1.8) - 459.67)
            print(f"{user}°K = {resultado:.2f}°F\n")
        
        # Pausa para o usuário ver o resultado antes de limpar a tela
        input("Pressione Enter para continuar...")
        
        # Limpa a tela
        os.system('cls' if os.name == 'nt' else 'clear')

conversor_de_temperatura()