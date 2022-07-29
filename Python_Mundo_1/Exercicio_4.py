# Crie um código que leia uma resposta do  usuário, identifique seu tipo primitivo e retorne na tela.


texto = input("Digite algo: ")

if texto.isnumeric() == True:
    print('Você digitou um número!')
else:
    print('Você digitou um texto!')