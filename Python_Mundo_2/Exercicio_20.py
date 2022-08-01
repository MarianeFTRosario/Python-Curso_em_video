# Crie um código que leia o gênero do usuário e aceite somente F e M. Em caso diferente, solicitei a informação novamente.


sexo = input('Informe o seu sexo: ').strip().lower()[0]

while sexo not in 'fm':
    sexo = input('Sexo inválido! Informe seu sexo novamente: ').strip().lower()[0]