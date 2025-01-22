# Entrada dos números
a = int(input("Informe o valor de 'a': "))
b = int(input("Informe o valor de 'b': "))

# Verificar se os números são positivos
if a < 0 or b < 0:
    print("Os valores não podem ser negativos!")
    exit()

# Garantir que a >= b
if a < b:
    a, b = b, a

# Algoritmo de Euclides
while b != 0:
    resto = a % b  # Calcula o resto da divisão
    a, b = b, resto  # Atualiza a e b

# Resultado final
print(f"O MDC é {a}")
