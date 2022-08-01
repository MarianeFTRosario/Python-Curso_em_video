# Escreve um código que leia um número, razão, e mostre as 10 primeiras progressões aritmética


numero = int(input('Informe um número inteiro: '))
razao = int(input('Informe a razão inteira: '))
count= 0

while count < 10:
    count += 1
    print(f'{numero} => ', end = '')
    numero += razao

print('Fim')