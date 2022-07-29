# Crie um programa que pergunte ao usuário a velocidade do carro. A partir disso calcule o valor da multa, considerando que a infração ocorrerá se o automóvel estiver acima de 80 km/h e que o motorista deve pagar 7,00 R$ a cada quilometro acima do limite permitido. 

velocidade = float(input('Informe a velocidade do veículo: '))

if velocidade > 80.00:
    print(f'Você foi multado! O valor da multa é {(velocidade - 80) * 7:.2f} reais')
else:
    print(f'Parabéns, você está dentro do limite de velocidade permitido. ')
