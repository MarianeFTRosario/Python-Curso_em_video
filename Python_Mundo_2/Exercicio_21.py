# Crie um jogo onde o usário deve acerta o número entre 0 e 10 randomizado pelo computador


from random import randint

count = 0
computador = randint(0, 10)
usuario = int(input('Informe o número escolhido: '))

while usuario != computador:
    print('Você errou :(')
    usuario = int(input('Tente novamente: '))
    count += 1
    
print(f'''\nVocê acertou :)
O número escolhido pelo computador foi {computador}
Foram necessarias {count} tentativas para a sua vitória.''')


#  Outra lógica para o jogo

from random import randint

computador = randint(0, 10)
acertou = False
count = 0

while not acertou:
    usuario = int(input('Qual seu palpite? '))
    count += 1 
    if usuario == computador:
        acertou = True
    else:
        if usuario < computador:
            print('Você errou! Tente um número maior: ')
        else:
            print('Você errou! Tente um número menor: ')
            
print(f'''\nVocê acertou :)
Foram necessárias {count} tentativas para a sua vitória.''')