# == DESAFIO 018 ==
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
# Observação: É necessário converter o valor do ângulo para radianos, para depois calcular o seno, coseno e tangente.

from math import radians, sin, cos, tan
angulo = float(input('Digite um ângulo qualquer: '))
seno = sin(radians(angulo))
coseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('- O ângulo de {:.2f}º tem o seno {:.2f}.'.format(angulo, seno))
print('- O ângulo de {:.2f}º tem o coseno {:.2f}'.format(angulo, coseno))
print('- O ângulo de {:.2f}º tem a tangente {:.2f}.'.format(angulo, tangente))
