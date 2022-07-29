# Escreva um programa que receba três números e informe qual o maior e qual o menor.


numero1 = float(input('Informe um número: '))
numero2 = float(input('Informe mais um número: '))
numero3 = float(input('Inform outro número: '))

if numero1 < numero2 and numero1 < numero3:
    print(f'{numero1} é o menor número informado.')
elif numero2 < numero1 and numero2 < numero3:
    print(f'{numero2} é o menor número informado.' )
else:
    print(f'{numero3} é o menor número informado.' )
    
if numero1 > numero2 and numero1 > numero3:
    print(f'{numero1} é o maior número informado.')
elif numero2 > numero1 and numero2 > numero3:
    print(f'{numero2} é o maior número informado.' )
else:
    print(f'{numero3} é o maior número informado.' )