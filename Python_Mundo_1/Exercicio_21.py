# Crie um código que leia vários nomes informados pelo usuário e os imprima fora da ordem informada.

import random

nomes = []
resposta = 's'

while resposta == 's':
    nome = input('Informe um nome: ')
    nomes.append(nome)
    resposta = input('Deseja informar mais um nome? ')

print(f'A lista aleatória é {random.shuffle(nomes)}')