# Crie um código que receba o ano de nascimento e informe se o usuário está no periódo de alistament0o, se o prazo já passou ou quando tempo falta para isso.


from datetime import date

ano_nascimento = int(input('Informe o ano do seu nascimento: '))
idade = (date.today().year - ano_nascimento)
if  idade < 18:
    print(f'Você ainda é menor de idade e não precisa se alistar. Ainda faltam {18 - idade} anos(s), volte em {date.today().year + (18 - idade)}')
elif idade > 18:
    print(f'O período do seu alistamento já passou. Você deveria ter se alistado em {date.today().year - (idade - 18)}, isso foi ha {idade - 18} anos')
else:
    print('Você está no período de alistamento, seja bem vindo.')