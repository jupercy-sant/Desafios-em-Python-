# == DESAFIO 017 ==
'''Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa.'''

# Primeira forma (sem importar biblioteca)
'''co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2 ) ** (1/2)
print('A hipotenusa vai medir {:.2f}.'.format(hi))'''


# Segunda forma
from math import hypot
oposto = float(input('Digite o comprimento do cateto oposto: '))
adjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = hypot(oposto, adjacente)
print('- A hipotenusa mede {:.2f}.'.format(hipotenusa))

