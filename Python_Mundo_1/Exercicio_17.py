# Crie um código que retorno a parte inteira de um número float informado pelo usuário.

# Código utilizando a biblioteca math

import math

numero = float(input('Olá, digite um número real: '))
print(f'A parte inteira do número digitado é {math.trunc(numero)}')


# Código sem utilização de biblioteca

numero = float(input('Olá, digite um número real: '))
print(f'A parte inteira do número digitado é {numero//1:.0f}')