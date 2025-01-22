def mmc(a, b):
    maior = max(a, b)
    while True:
        if maior % a == 0 and maior % b == 0:
            return maior
        maior += 1

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

imc = mmc(num1, num2)
print(f"O MMC de {num1} e {num2} é {imc}")
