# Escreva um código que leia produtos comprados pelo usuário e ao final informe o valor total, quantos produtos custam mais de 1.000 reias e qual o produto mais barato.


soma = produtos_caros = count = 0
resposta = 's'

while True:
    if resposta == 's':
        produto = input('Informe o produto: ')
        preco = float(input('Informe o valor do produto: '))
        soma += preco
        if preco > 1000:
            produtos_caros += 1
        if count == 0:
            maior_produto = produto
            maior = preco
            menor_produto = produto
            menor = preco
        else:
            if preco < menor:
                menor = preco
                menor_produto = produto
            if preco > maior:
                maior = preco
                maior_produto = produto
        count += 1
    else:
        break
        
    resposta = input('Deseja cadastrar outro produto? ').strip().lower()[0]
    
    
print(f'''\nVocê comprou {count} produtos.
Sua compra deu {soma:.2f}.
O produto mais barato foi o {menor_produto} no valor de R${menor} e o mais caro o {maior_produto} no valor de R${maior}.
Você comprou {produtos_caros} produtos acima de mil reias''')