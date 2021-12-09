# == DESAFIO 023 ==
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

numero = int(input('Digite um número inteiro qualquer: '))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('No número {}...'.format(numero))
print('A unidade é {};'.format(u))
print('A dezena é {};'.format(d))
print('A centena é {};'.format(c))
print('E o milhar é {}.'.format(m))

