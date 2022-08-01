# Escreva um código que calcule o preço de um produto de acordo com a opção de pagamento, que podem ser: a vista no dinheiro com 10% de desconto, a vista no cartão com 5% de desconto, 2 vezes no cartão preço normal e acima de 2 vezes no cartão com 20% juros.


print ('===== Loja Python =====')

preco = float(input('Informe o preço do produto: '))
print('''Opção de pagamento:
[ 1 ] Dinheiro
[ 2 ] A vista no cartão
[ 3 ] 2x no cartão
[ 4 ] Acima de 3x no cartão
''')
opcao_pagamento = int(input('Opção de pagamento: '))

if opcao_pagamento == 1:
    print(f'Essa opção de pagamento tem 10% de desconto. Por isso o valor final do produto é {preco - (preco * (10/100)):.2f} reais.')
elif opcao_pagamento == 2:
    print(f'Essa opção de pagamento tem 5% de desconto. Por isso o valor final do produto é {preco - (preco * (5/100)):.2f} reais.')
elif opcao_pagamento == 3:
    print(f'Essa opção de pagamento não tem desconto. Por isso o valor final do produto é {preco:.2f} reais. O pagamento será em 2 vezes de {preco / 2}')
elif opcao_pagamento == 4:
    parcelas = int(input('Informe a quantidade de parcelas: '))
    print(f'Essa opção de pagamento tem 20% de juros. Por isso o valor final do produto é {preco + (preco * (20/100)):.2f} reais. O pagamento será em {parcelas} vezes de {(preco + (preco * (20/100))) / parcelas}')
else:
    print('Essa opção de pagamento não existe.')