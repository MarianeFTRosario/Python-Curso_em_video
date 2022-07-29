# Crie um código que leia quantos dias o usuário alugou um carro e quanto quilometros ele percorreu com o mesmo. Calcule o preço a ser pago sabendo que o valor do aluguel por dia é de 60 reais e cada quilimetro rodado custa 0,15.

dias = int(input('Informe a quantidade de dias que o carro ficou alugado: '))
quilometros = float(input('Informe quantos quilometros foram rodados: '))

print(f'O valor pago por {dias} dias de aluguel é R$ {dias * 60:.2f} e o valor pago por {quilometros:.2f} quilometros rodados é R$ {quilometros * 0.15:.2f}. O total a ser pago é de R$ {(dias * 60) + (quilometros * 0.15):.2f}')