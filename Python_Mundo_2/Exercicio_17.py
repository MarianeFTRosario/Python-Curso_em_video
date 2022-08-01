# Escreva um códgio que leia o ano de nascimento de 7 pessoas e informe quantas delas são maiores de idade,


from datetime import date

maiores_idade = 0
menores_idade = 0

for i in range(1, 8):
    ano_nascimento = int(input(f'Informe o ano de nascimento da {i} pessoas: '))
    if date.today().year - ano_nascimento > 18:
        maiores_idade += 1
    else:
        menores_idade += 1

print(f'São {maiores_idade} pessoas maiores de idade e {menores_idade} menores de idade.')