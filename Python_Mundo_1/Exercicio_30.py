# Crie um código que receba duas notas e calcule a média. O programa deve retornar uma mensagem dizendo que a nota foi boa se a média tiver sido maior ou igual a seis, se menor, informar que é necessário estudar mais.

nota1 = float(input('Informe a primeiro nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2) / 2
print(f'A média das suas notas é {media:.1f}')

if media >= 6.0:
    print('Sua média está boa. Parabéns!')
else:
    print('Sua média não está boa. É necessário estudar mais!')