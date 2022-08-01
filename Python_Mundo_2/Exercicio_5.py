# Crie um código que leia a idade do usuário e informe qual a categoria de natação ele deve se inscrever. As faixas são: até 9 anos mirim, até 14 anos infantil, até 19 anos júnior, até 25 anos master, acima de 25 anos sênior.

from datetime import date

ano_nascimento = int(input('Informe o ano de nascimento: '))
idade = date.today().year - ano_nascimento

if idade <= 9:
    print(f'Você tem {idade}, e está na categoria mirim')
elif idade <= 14:
    print(f'Você tem {idade}, e está na categoria infatil')
elif idade <= 19:
    print(f'Você tem {idade}, e está na categoria júnior')
elif idade <= 25:
    print(f'Você tem {idade}, e está na categoria sênior')
else:
    print(f'Você tem {idade}, e está na categoria master')