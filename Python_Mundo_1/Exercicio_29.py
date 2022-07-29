# Faça um código que leia o nome do usuário e, se o mesmo for Mariane, faça um elogio, se não escreva 'Seu nome é tão normal'. Ao final o programa deve dar boas vindas.


nome = input('Olá, qual o seu nome: ').strip().capitalize()

if nome == 'Mariane':
    print('Uau, que nome lindo.')
else:
    print('Que nome normal.')
    
print(f'Seja bem vindo(a), {nome}!')