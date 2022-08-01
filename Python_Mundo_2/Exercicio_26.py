# Crie um código que leia vários números e só pare quando o usuário digitas 999. Após o fim do código o mesmo deve mostrar quantos números foram digitos e a soma deles, sem incluir o 999.


numero = float(input('Informe um número: '))
count = 0
soma = 0

while numero != 999:
        count += 1
        soma += numero
        numero = float(input('Informe um número: '))

print(f'Você digitou {count} números e a soma deles é {soma:.2f}')

# Lógica utilizando o comando break


numero = count = soma = 0

while True:
    numero = int(input('Informe um número inteiro: '))
    if numero == 999:
        break
    count += 1
    soma += numero
    
print(f'Você digitou {count} e a soma deles é {soma}.')