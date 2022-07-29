# Crie um jogo que escolha aleatoriamente um número entre 0 e 5, e peça para o usuário adivinhar. Se o mesmo acertar de parabéns, caso contrário, que errou.

from random import randint

numero_computador = randint(0, 5)
numero_usuario = int(input('Informe o número inteiro: '))

if numero_usuario == numero_computador:
    print('Parabéns! Você acertou. :)')
else:
    print(f'Errou! O número correto é {numero_computador}')