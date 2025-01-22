import os

def conversor_de_temperatura():
    
    while True:
        # 1. Menu de opções
        print("=== Conversor de Temperaturas ===".center(40, "="))
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
            print("Escolha uma opção válida entre 1 e 7!")
            input("Pressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        
        # Solicita os dois valores para a operação
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
            # Se o usuário inserir um valor inválido, exibe uma mensagem de erro e reinicia o loop
            print("Por favor, insira números válidos.")
            input("Pressione Enter para continuar...")
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        
        if opcao in [3, 4, 6] and user < 0:
            print("O valor em Kelvin não pode ser negativo!")
            input("Pressione Enter para continuar...")
            continue
            
        # Executa a operação escolhida
        if opcao == 1:
            # Celsius para Fahrenheit
            resultado = float((user * 9/5) + 32 )
            print(f"Conversão concluida!\n{user}°C convertido em Fahrenheit é {resultado:.2f}°F\n")
        elif opcao == 2:
            # Fahrenheit para Celsius
            resultado = (user - 32) / 1.8
            print(f"Conversão concluida!\n{user}°F convertido em Celsius é {resultado:.2f}°C\n")
        elif opcao == 3:
            # Celsius para Kelvin
            resultado = user + 273.15
            print(f"Conversão concluida!\n{user}°C convertido em Kelvin é {resultado:.2f}°K\n")
        elif opcao == 4:
            # Kelvin para Celsius
            resultado = user - 273.15
            print(f"Conversão concluida!\n{user}°K convertido em Celsius é {resultado:.2f}°C\n")
        elif opcao == 5: 
            # Fahrenheit para Kelvin 
            resultado = ((user + 459.67) * 5) / 9
            print(f"Conversão concluida!\n{user}°F convertido em Kelvin é {resultado:.2f}°K\n")
        elif opcao == 6:
            # Kelvin para Fahrenheit
            resultado = (user * 1.8) - 459.67
            print(f"Conversão concluida!\n{user}°K convertido em Fahrenheit é {resultado:.2f}°F\n")
        
        # Pausa para o usuário ver o resultado antes de limpar a tela
        input("Pressione Enter para continuar...")
        
        # Limpa a tela
        os.system('cls' if os.name == 'nt' else 'clear')

conversor_de_temperatura()