# Escreva um código que receba dois números e informe qual é o maior, o menor ou se eles são iguais. 

numero1 = float(input('Informe o primeiro número: '))
numero2 = float(input('Inform o segundo número: '))

if numero1 > numero2:
    print(f'O número {numero1} é maior que o número {numero2}')
elif numero1 < numero2:
    print(f'O número {numero2} é maior que o número {numero1}')
else:
    print(f'Os números {numero1} e o {numero2} são iguais')