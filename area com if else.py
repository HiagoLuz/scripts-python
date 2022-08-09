b = int(input('Digite o valor da base do retângulo: '))

a = int(input('Digite o valor da altura do retângulo: '))

area = b * a

print("O valor da area do retângulo é:", area)

if area>100:
    print("Terreno Grande")
else:
    print("Terreno Pequeno")