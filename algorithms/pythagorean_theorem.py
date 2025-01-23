cateto_a = float(input("Informe cateto a: "))
cateto_b = float(input("Informe cateto b: "))

def pythagorean_theorem():
    hipotenusa = (cateto_a**2+ cateto_b**2)**0.5
    return hipotenusa

print(pythagorean_theorem())