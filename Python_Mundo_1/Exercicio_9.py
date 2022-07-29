# Crie um código que leia um número informado pelo usuário e retorne sua tabuada.

# Tabuada feita com um código simples.

numero = int(input("Informe um número: "))

print(f"""{numero} * 1 = {numero * 1}
{numero} * 2 = {numero * 2}
{numero} * 3 = {numero * 3}
{numero} * 4 = {numero * 4}
{numero} * 5 = {numero * 5}
{numero} * 6 = {numero * 6}
{numero} * 7 = {numero * 7}
{numero} * 8 = {numero * 8}
{numero} * 9 = {numero * 9}
{numero} * 10 = {numero * 10}
""")

# Tabuada mais eficiente e com código mais exuto.

numero = int(input("informe um número: "))
contador = 1

while contador <= 10:
    print(f'{numero} * {contador} = {numero * contador}')
    contador = contador + 1