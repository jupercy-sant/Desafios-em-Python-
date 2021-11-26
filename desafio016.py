# == DESAFIO 016 ==
# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua parte inteira.

# Primeira forma
'''from math import trunc
numreal = float(input('Digite um número: '))
partint = trunc(numreal)
print('O número {} tem como parte inteira o número {}.'.format(numreal, partint))'''

# Segunda forma (sem importar biblioteca)
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é o {}.'.format(num, int(num)))
