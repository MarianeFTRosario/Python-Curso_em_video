# Crie um código que leia vários nomes informados pelo usuário, e ao final sortei um aleatoriamente. 

import random

nomes = []
resposta = 's'

while resposta == 's':
    nome = input('Informe um nome: ')
    nomes.append(nome)
    resposta = input('Deseja informar mais um nome? ')
    
    
escolhido = random.choice(nomes)
print(f'O nome escolhido é {escolhido}')