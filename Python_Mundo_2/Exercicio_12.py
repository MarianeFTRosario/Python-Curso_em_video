# Escreva um código que faça uma tabuada de multiplicação de um número escolhido pelo usuário.


tabuada = int(input('Escolha o número que seja fazer a tabuada: '))

for i in range(0, 11):
    print(f'{tabuada} x {i} = {tabuada * i}')