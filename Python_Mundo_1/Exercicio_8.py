# Crie um código que receba um valor em metros informado pelo usuário, transforme-o em centimetro e milimetros e imprima os valores em tela.

metros = float(input("Informe o valor em metros: "))

print(f"A conversão do valor em centímetros é {metros * 100:.0f}, e em milímetro é {metros * 1000:.0f}")