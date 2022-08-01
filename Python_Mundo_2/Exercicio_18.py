# Escreva um código que leia o peso de 5 pessoas e mostre qual é o maior e qual é o menor.


menor = 0
maior = 0

for i in range(1, 6):
    peso = float(input(f'Informe o peso da {i} pessoa: '))
    if i == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O menor peso é {menor} e o maior é {maior}')