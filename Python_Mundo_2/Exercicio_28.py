# Escreva um código que faça a tabuada de multiplicação de um número informado pelo usuário e só pare se o mesmo informar um valor negativo.


while True:
    numero = int(input('\nQuer ver a tabuada de qual valor? '))
    if numero < 0:
        break
    for i in range(1,11):
        print(f'{numero} x {i} = {numero * i}')

print('\nPrograma encerrado')