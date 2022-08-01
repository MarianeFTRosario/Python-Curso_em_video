# Escreva um código de aprovação de empréstimo para compra de imóveis. O programa deve receber o valor da compra, o salário do comprador e em quantos anos deseja pagar. Para a aprovação do empréstimo o valor da parcela deve ser menor que 30% do salário do usuário.


nome = input('Informe seu nome: ').strip()
valor_imovel = float(input('Informe o valor do imóvel: '))
salario = float(input('Informe o valor do seu salário: '))
tempo_pagamento = int(input('Informe em quatos anos você deseja pagar: '))
prestacao = valor_imovel / (tempo_pagamento * 12)

if prestacao <= (salario * (30 / 100)):
    print(f'{nome}, Sua prestação é de {prestacao:.2f} reais. Compra aprovada com sucesso! Aproveite seu imóvel')
else:
    print(f'{nome}, Sua prestacao é de {prestacao:.2f} reais. Infelizmente sua compra não foi aprovado, pois seu salário não é compatível com o valor a ser pago.')