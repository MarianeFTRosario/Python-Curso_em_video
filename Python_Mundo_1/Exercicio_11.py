# Crie um código que calcule a área de uma pareda informada pelo usuário e informe a quantidade de tinta necessaria para pinta-la. Para o exercício considere que cada litro pinte dois metros de área.


altura = float(input('Informe a altura da parede: '))
largura = float(input('Informe a largura da parede: '))
area = altura * largura

print(f'Uma parede com {altura:.0f} de altura e {largura:.0f} de largura, possuí uma área de {area:.0f}m². Para pinta-la será necessário {area / 2:.0f} litros de tinta')