# Crie um código que leia o valor de um produto, o desconto a ser aplicado e retorne o valor a ser pago no final.

preco = float(input('Informe o valor do produto: '))
desconto = float(input('Informe o percentual do desconto: '))

print(f'O valor de {preco:.0f} reais aplicado a um desconto de {desconto:.0f}% terá um preço final de {preco - preco * (desconto / 100):.0f} reais.')