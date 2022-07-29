# Escreva um código que leia o nome completo do usuário e verifique se possuí palavra 'silva' e retorne essa informação.

nome = input('Informe seu nome completo: ')
retorno = 'silva' in nome.lower()

print(f'Possuí Silva no nome? {retorno}')