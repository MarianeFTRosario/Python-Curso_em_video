# Crie um código que receba peso e altura do usuário, calcule o IMC e, informe ao usuário qual o seu quadro. Considerando que abaixo de 18,50 é abaixo do peso, entre 18,50 e 25 peso ideal, entre 25 a 30 sobrepeso, 30 a 40 obesidade e acima de 40 obesidade mórbida.


peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura ** 2)

if imc < 18.50:
    print(f'Seu IMC é {imc:.2f}. Você está abaixo do peso.')
elif imc < 25:
    print(f'Seu IMC é {imc:.2f}. Você está com o peso ideal.')
elif imc < 30:
    print(f'Seu IMC é {imc:.2f}. Você está com sobrepeso.')
elif imc < 40:
    print(f'Seu IMC é {imc:.2f}. Você está com obesidade.')
else:
    print(f'Seu IMC é {imc:.2f}. Você está com obesidade morbida.')