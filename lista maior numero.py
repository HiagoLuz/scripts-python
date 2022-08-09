numeros = []
 
for i in range(0, 9, 1):
    x = int(input('Digite um numero: '))
    numeros.append(x)
print("O maior numero é:")
print(max(numeros, key=int))    