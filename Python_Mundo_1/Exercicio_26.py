# Escreva um código que leia uma frase e calcule quantas palavras 'a' existem e também infome a primeira e última posição que elas ocupam.


frase = input('Digite uma frase: ').strip().lower()

print(f'''Na frase existem {frase.count('a')} letras \"A\"
A primeira letra \"A\" aperece na posição {frase.find('a') + 1}
A última letra \"A\" aparece na posição {frase.rfind('a') + 1}
''')