# Crie uma lógica que leia vários números inteiros, calcule a média, qual é o menor e o maior  número e, só pare quando o usuário quiser.


resposta = 's'
soma = 0
count = 0
media = 0
while resposta == 's':
    numero = int(input('Informe um número inteiro: '))
    soma += numero
    count += 1
    if count == 1:
        menor = numero
        maior = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    resposta = input('Deseja informa mais números? S ou N: ').strip().lower()[0]

media = soma / count
print(f'Você digitou {count} números e a média entre eles é de {media}. E o menor número informado é {menor} e o maior é {maior}')