def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
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

# Entrada de dados
peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m): "))

# Cálculo do IMC
imc = calcular_imc(peso, altura)
classificacao = classificar_imc(imc)

# Resultado
print(f"Seu IMC é {imc:.2f}. Classificação: {classificacao}")
