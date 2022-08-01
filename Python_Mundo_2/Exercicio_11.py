# Crie um código que mostre a soma dos números ímpares que sejam multiplos de 3 e, que estejam no intervalo de 1 até 500.


soma = 0
count = 0

for i in range (1, 501):
    if (i % 2) != 0 and (i % 3) == 0:
        soma = soma + i
        count = count + 1
        
print(f'A soma dos {count} numeros impares multiplos de 3 é igual a {soma}')