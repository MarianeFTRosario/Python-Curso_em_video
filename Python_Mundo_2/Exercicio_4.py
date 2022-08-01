# Crie um programa que receba duas notas, calcule a média e retorne a situação do aluno. Se a média for abaixo de 5 o status é reprovado, entre 5 e 6.9 está de recuperação e se maior que 7 aprovado.


nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5: 
    print (f'Sua média é {media:.1f}. Infelizmente você está reprovado. :(')
elif media >= 5 and media < 7: # Essa condição também pode ser representada assim: 5 <= media < 7
    print(f'Sua média é {media:.1f}. Infelizmente você está em recuperação. Bora que ainda da tempo.')
else:
    print (f'Sua média é {media:.1f}. Parabéns, você está aprovado. :) ')