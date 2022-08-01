# Escreva um código que simule um caixa eletrónico. O programa deve perguntas ao usuário quanto ele quer sacar e informe a quantidade de notas entregues, considerando que a disponível as notas de 50, 20, 10 e 1


saque = int(input('Informe o valor do saque: '))
calculo = saque

while True:
    if saque >= 50:
        nota_cinquenta = saque // 50
        print(f'{nota_cinquenta} cedulas de R$50,00')
        saque -= (nota_cinquenta * 50)
    elif saque >= 20:
        nota_vinte = saque // 20
        print(f'{nota_vinte} cedulas de R$20,00')
        saque -= (nota_vinte * 20)
    elif saque >= 10:
        nota_dez = saque // 10
        print(f'{nota_dez} cedulas de R$10,00')
        saque -= (nota_dez * 10)
    elif saque >= 1:
        nota_um = saque // 1
        print(f'{nota_um} cedulas de R$ 1,00')
        saque -= (nota_um * 1)
    else:
        break