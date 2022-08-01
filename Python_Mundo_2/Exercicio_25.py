# Escreva um código que leia um número, razaão e mostre as 10 primeiras progressões aritmética. Após isso pergunte ao usuário deseja ver mais progressões e quantos ele deseja.


numero = float(input('Informe um número: '))
razao = float(input('Informe a razão: '))
count = 0
projecao = 10
escolha = 's'


while escolha == 's':
    while count < projecao:
        count += 1
        print(numero)
        numero += razao
    escolha = input('Você deseja ver mais projeções aritméticas desse número? S ou N? ').strip().lower()
    if escolha == 's':
        count = 0
        projecao = float(input('informe quantas projeções deseja ver:'))