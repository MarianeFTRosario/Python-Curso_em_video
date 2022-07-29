# Crie um código que leia ângulo e calcule o seu seno, cosseno e tangente.

import math

angulo = float(input('Informe o ângulo: '))

print(f'''Para o ângulo informado temos as seguintes medidas:
Seno: {math.sin(math.radians(angulo)):.2f}
Cosseno: {math.cos(math.radians(angulo)):.2f}
Tangente: {math.tan(math.radians(angulo)):.2f}
''')