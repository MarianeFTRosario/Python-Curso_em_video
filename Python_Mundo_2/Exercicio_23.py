# Escreva um código que leia um número e calcule o seu fatorial.


from math import factorial

numero = int(input('Informe um número: '))
print(f'O resultado da fatoração é {factorial(numero)}')



# Códgios sem a biblioteca math


numero = int(input('Informe um número inteiro: '))
count = numero
fatorial = 1

while count > 0:
    print(f'{count}', end = '')
    print(' x '
           if count > 1
           else ' = ', end = '')
    fatorial *= count
    count -= 1
    
print(f'{fatorial}')

# ------------------------------------------------------------------

numero = int(input('Informe um número inteiro: '))

for i in range(numero - 1, 0, -1):
    numero *= i
print(f'O resultado da fatoração é {numero}')