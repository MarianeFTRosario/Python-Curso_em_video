# Crie uma lógica que leia a idade e o gênero de vários usuários e calcule quantas possuem mais de 18 anos, quantos homens foram cadastrados e quantas mulheres tem menos de 20 anos


maiores_de_idade = homens = mulheres_menores = 0
resposta = 's'

while True:
    if resposta == 's':
        idade = int(input('Informe a idade: '))
        sexo = input('Informe o sexo: ').strip().lower()[0]
        if sexo  not in 'fm':
            sexo = input('Informe o sexo: ').strip().lower()[0]
        if idade >= 18:
            maiores_de_idade += 1
        if sexo == 'm':
            homens += 1
        if sexo == 'f' and idade < 20:
            mulheres_menores += 1
    elif resposta == 'n':
        break
    else:
        resposta = input('Deseja cadastrar mais usuários: ').strip().lower()[0]
        
    resposta = input('Deseja cadastrar mais usuários: ').strip().lower()[0]
    
print(f'Você cadastrou {maiores_de_idade} pessoas maiores de idade, {homens} homens e {mulheres_menores} mulheres menores de idade;')