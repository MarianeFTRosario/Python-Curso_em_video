# Crie um código que calcule aumento de salários. Se o valor informado for maior que 1.250,00 R$ o aumento deve ser de 10% se menor 10%


salario = float(input('Informe o seu salário: '))

if salario > 1250:
    novo_salario = salario + ((10 / 100) * salario)
    print(f'Seu salário com aumento será {novo_salario:.2f}')
else:
    novo_salario = salario + ((15 / 100) * salario)
    print(f'Seu salário com aumento será {novo_salario:.2f}')