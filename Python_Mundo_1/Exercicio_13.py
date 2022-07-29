# Crie um código que leia o salário e o aumento a ser aplicado, e informe o valor final.

salario = float(input('Informe o valor do salário: '))
aumento = float(input('Informe o percentual do aumento: '))

print(f'Um salário de {salario:.0f} reais com {aumento:.0f}% de aumento ficará {salario + salario * (aumento / 100):.0f}')