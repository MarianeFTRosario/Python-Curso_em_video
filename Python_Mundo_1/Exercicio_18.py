# Crie um código que receba os valores de um triangulo e calcule sua hipotenusa. 

import math

# Código utilizando a raiz quadrada.

adjacente = float(input('Informe o cateto adjacente: '))
oposto = float(input('Informe o cateto oposto: '))
hipotenusa = math.sqrt((adjacente ** 2) + (oposto ** 2))

print(f'A hipotenusa do triangulo informado é {hipotenusa:.2f}')

# Código utilizando o metodo hypot da biblioteca math.

adjacente = float(input('Informe o cateto adjacente: '))
oposto = float(input('Informe o cateto oposto: '))

print(f'A hipotenusa do triangulo informado é {math.hypot(oposto, adjacente):.2f}')