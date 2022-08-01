# Escreva um código que retorne os 10 primeiros números de uma progressão aritmética. Para isso peça ao usuário o número inicial e a razão.

numero = float(input('Informe o início da progressão: '))
razao = float(input('Informe a razão: '))

for i in range (0, 10):
    print(numero)
    numero = numero + razao