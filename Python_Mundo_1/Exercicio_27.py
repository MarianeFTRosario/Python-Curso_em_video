# Crie um código que leia o nome completo do usuário e retorno apenas o primeiro e último nome.

nome = input('Informe seu nome completo: ').strip()

print(f'''Seu primeiro nome é: {nome.split()[0]}
Seu último nome é: {nome.split()[-1]}
''')