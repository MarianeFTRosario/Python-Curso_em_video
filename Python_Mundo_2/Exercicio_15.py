# Escreva um código que receba um número e informe se ele é ou não um número primo.


numero = int(input('Informe um número inteiro: '))
primos = 0

for i in range (1, numero + 1):
    if numero % i == 0:
        primos += 1

if primos == 2:
    print('Esse número é primo.')
else:
    print('Esse número não é primo')