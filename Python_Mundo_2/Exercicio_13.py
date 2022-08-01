# Crie um código  que leia 6 números e faça a soma apenas do números pares.


soma = 0
count = 0

for i in range(1, 7):
    numero = int(input(f'Informe o {i} o inteiro: '))
    if (numero % 2) == 0:
        soma += numero
        count += 1
        
print(f'Você informou {count} números pares e a soma deles é {soma}')