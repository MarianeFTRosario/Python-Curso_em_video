# Escreva um código que calcule o custo de uma passagem, para isso considere que se o trajeto for de até 200 km o custo de cada quilometro deve ser 0,50 se maior 0,45


quilometro = float(input('Informe quantos quilometros tem a viagem: '))

if quilometro <= 200.00:
    print(f'O preço da sua passagem é {quilometro * 0.50:.2f} reais')
else:
    print(f'O preço da sua passagem é {quilometro * 0.45:.2f}')