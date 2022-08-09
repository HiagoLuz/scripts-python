for i in range(0, 20, 1):
    x = input('Digite um numero: ')
    arquivo = open(r"c:\Users\hiago\OneDrive\Área de Trabalho\Python\Ex33.py.txt", 'a')
    arquivo.writelines(x + '\n')
    arquivo.close()

import x

lista = [1, 2, 3, 4, 5]
resultado = x.prod(Numeros)
print(resultado)