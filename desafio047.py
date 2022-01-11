# == DESAFIO 047 ==
# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

# Nessa primeira maneira, é utilizado um if indicando que caso o número seja divisível por 2 esse número será mostrado.
# O problema é que o computador acaba fazendo o dobro de laços antes de mostrar o número (indicado pelo print do ponto.)
#
"""
print('Números pares entre 1 e 50')
for numero in range(0, 51):
    print('.', end='')
    if numero % 2 == 0:
        print(numero, end=' ')
print('Fim')
"""

# Nessa segunda maneira, o programa gera metade das repetições.
for numero in range(0, 51, 2):
    print(numero, end=' ')
print('Acabou')