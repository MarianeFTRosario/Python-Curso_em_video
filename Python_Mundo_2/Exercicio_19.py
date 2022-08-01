# Escreva um código que leia a nome, idade e gênero de 4 pessoas e mostre qual a média de idade do grupo, o nome do homem mais velho e quantas mulheres tem menos de 20 anos.


soma_idade = 0
maior = 0
mulheres_maiores = 0

for i in range(1, 5):
    nome = input(f'Informe o nome da {i} pessoa: ').strip()
    idade = int(input(f'Informe a idade da {i} pessoa: '))
    sexo = input(f'Informe o sexo da {i} pessoas: F: feminino e M: Masculino: ').strip().lower()  
    soma_idade += idade
    if sexo == 'm':
        if idade > maior:
            homem_velho = nome
    else:
        if idade <= 18:
            mulheres_maiores = mulheres_maiores + 1
    
print(f'''A média das idade é {soma_idade / 4:.2f}
O home mais velho se chama {homem_velho}
A quantidade de mulheres menores de idade é {mulheres_maiores}
''')