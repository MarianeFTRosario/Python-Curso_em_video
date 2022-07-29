# Escreva um código que leia o nome do usuário e retorne-o com todas as letras maíusculas e minusculas e, também informe a quantidade de letras do primeiro nome e do nome completo.


nome = input('Informe seu nome completo: ').strip()

print(f'''Nome maíusculo: {nome.upper()}
Nome mínusculo: {nome.lower()}
Quantidade de letras: {len(nome) - nome.count(" ")}
Quantidade de letras do primeiro nome: {len(nome.split()[0])}
''')