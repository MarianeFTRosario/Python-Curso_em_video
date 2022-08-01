# Escreva um código que jogue jokenpô com o usuário.

from random import choice

opcoes = ['pedra', 'papel', 'tesoura']
computador = choice(opcoes)
print(''' ===== Jokenpô =====
- Pedra
- Papel
- Tesoura
''')

usuario = input('Informe sua jogada: ').strip().lower()


if computador == 'pedra':    
    if usuario == 'papel':
        print(f'Computador escolheu {computador} e você {usuario}. Você ganho \o/')
    elif usuario == 'tesoura':
        print(f'Computador escolheu {computador} e você {usuario}. Você perdeu :(')
    elif usuario == 'tesoura':
        print(f'Computador escolheu {computador} e você {usuario}. Deu empate!')
    else:
        print('Sua jodada é inválida.')
elif computador == 'papel':              
    if usuario == 'pedra':
        print(f'Computador escolheu {computador} e você {usuario}. Você perdeu :(')
    elif usuario == 'tesoura':
        print(f'Computador escolheu {computador} e você {usuario}. Você ganho \o/')
    elif usuario == 'papel':
        print(f'Computador escolheu {computador} e você {usuario}. Deu empate!')
    else:
        print('Sua jogada é inválida.')

else:
    if usuario == 'pedra':
        print(f'Computador escolheu {computador} e você {usuario}. Você ganho \o/')
    elif usuario == 'papel':
        print(f'Computador escolheu {computador} e você {usuario}. Você perdeu :(')
    elif usuario == 'pedra':
        print(f'Computador escolheu {computador} e você {usuario}. Deu empate!')
    else:
        print('Sua jogada é inválida')