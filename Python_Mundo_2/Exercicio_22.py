# Crie um código que recebe dois número do usuário e ofereça um menu com as opção matematicas disponíveis 


escolha = 0

numero1 = float(input('Informe o primeiro número '))
numero2 = float(input('Informe o segundo número: '))

while escolha != 5:
    escolha = int(input('''\n===== Menu =====
    [ 1 ] Realizar soma
    [ 2 ] Realizar multiplicação
    [ 3 ] Saber qual é o menor e qual é o maior
    [ 4 ] Infomar novos números
    [ 5 ] Sair do programa
    \n'''))
    
    if escolha == 1:
        print(f'\nA soma de {numero1} + {numero2} é {numero1 + numero2}')
    elif escolha == 2:
        print(f'\nA multiplicação de {numero1} x {numero2} é {numero1 * numero2}')
    elif escolha == 3:
        if numero1 > numero2:
            maior = numero1
            menor = numero2
        else:
            maior = numero2
            menor = numero1
        print(f'\nO número {maior} é maior que {menor}')
    elif escolha == 4:
        numero1 = float(input('Informe o primeiro número: '))
        numero2 = float(input('Informe o segundo número: '))
    elif escolha == 5:
        print('\nPrograma Finalizado')
    else:
        print('\nOpção inválida! Tente novamente')