# Escreva um código que leia uma palavra ou frase e diga se ela é um palíndromo.


frase = input('Escreva uma palavra ou frase: ').strip().lower()

if frase.replace(' ', '') == frase.replace(' ', '')[::-1]:
    print('Essa frase é palíndroma')
else:
    print('Essa frase não é palindroma')