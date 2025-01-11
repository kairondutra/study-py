import os

def calculadora_de_dois_valores(): 
    # Loop infinito para permitir múltiplas operações até o usuário decidir sair
    while True:
        # Exibe o menu de operações disponíveis
        print("Calculadora Simples")
        print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Sair")
        
        # Validação da operação escolhida pelo usuário
        try:
            operacao = int(input("Informe uma operação (1-5): "))
        except ValueError: 
            # Se o usuário inserir um valor inválido, exibe uma mensagem de erro e reinicia o loop
            print("Por favor, informe um valor válido.")
            input("Pressione Enter para continuar...")
            os.system('cls')
            continue
        
        # Verifica se o usuário escolheu sair
        if operacao == 5:
            print("Encerrando...")
            break
        
        # Verifica se a operação escolhida é válida (1-4)
        if operacao not in [1, 2, 3, 4]:
            print("Operação inválida. Escolha uma das opções (1-5).")
            input("Pressione Enter para continuar...")
            os.system('cls')
            continue
        
        # Solicita os dois valores para a operação
        try:
            numero1 = float(input("Informe o primeiro valor: "))
            numero2 = float(input("Informe o segundo valor: "))
        except ValueError:
            # Se o usuário inserir um valor inválido, exibe uma mensagem de erro e reinicia o loop
            print("Por favor, insira números válidos.")
            input("Pressione Enter para continuar...")
            os.system('cls')
            continue
            
        # Executa a operação escolhida
        if operacao == 1:
            # Soma
            resultado = numero1 + numero2
            print(f"= {resultado}\n")
        elif operacao == 2:
            # Subtração
            resultado = numero1 - numero2
            print(f"= {resultado}")
        elif operacao == 3:
            # Multiplicação
            resultado = numero1 * numero2
            print(f"= {resultado}")
        elif operacao == 4:
            # Divisão
            if numero2 == 0:
                # Verifica se o divisor é zero para evitar divisão por zero
                print("Erro: Divisão por zero não é permitida.")
            else:
                resultado = numero1 / numero2
                print(f"= {resultado}")
        
        # Pausa para o usuário ver o resultado antes de limpar a tela
        input("Pressione Enter para continuar...")
        
        # Limpa a tela
        os.system('cls')

# Chama a função para iniciar a calculadora
calculadora_de_dois_valores()