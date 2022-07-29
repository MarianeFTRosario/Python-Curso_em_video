# Crie um código que leia um número de 0 a 9999 e retorno qual é a unidade, dezena, centena e milhar do número informado.

numero = int(input('Informe um número de 0 a 9999: '))

print(f'''A unidade é {numero // 1 % 10}
A dezena é: {numero // 10 % 10}
A centena é: {numero // 100 % 10}
O milhar é: {numero // 1000 % 10}
''')