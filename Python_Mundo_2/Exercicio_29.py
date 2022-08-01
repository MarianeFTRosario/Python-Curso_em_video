# Crie um jogo de par ou ímpar com o computador. O programa só sera interrompido se o usuário perder


from random import randint

count = 0

while True:
    computador = randint(0,10)
    escolha_usuario = input('Impar ou Par ?').strip().lower()[0]
    usuario = int(input('Informe um número inteiro: '))
    
    resultado = (computador + usuario) % 2
    while escolha_usuario not in 'pi':
        escolha_usuario = input('Impar ou Par ?').strip().lower()[0]
    if resultado == 0:
        print(f'\nVocê jogou {usuario} e o computador {computador}')
        if escolha_usuario == 'p':
            print('Você ganhou. :)')
            count += 1
        else:
            print('Você perdeu. :(')
            break
    else:
        print(f'\nVocê jogou {usuario} e o computador {computador}')
        if escolha_usuario == 'i':
            print('Você ganhou. :)')
            count += 1
        else:
            print('você perdeu. :(')
            break
            
print(f'Você venceu {count} vezes')