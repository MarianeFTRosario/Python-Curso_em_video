# Escreva um código que leia a cidade informada pelo usuário e verifique se começa com a palavra 'santo' e retorne essa informação.

cidade = input('Informe o nome da sua cidade: ').strip()
retorno = cidade.lower().split()[0] == 'santo'

print(f'O nome da sua cidade começa com Santo? {retorno} ')