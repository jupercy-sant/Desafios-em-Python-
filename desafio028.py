# == DESAFIO 028 ==
'''Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça
para o usuário tentar descobrir qual foi o número escolhido pelo computador.'''
from random import randint
from time import sleep

n1 = randint(0, 5) # Faz o computador sortear um número.
print('-=-' * 19)
print('=*' * 9, 'JOGO DE ADIVINHAÇÃO', '*=' * 9)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar... ')
print('-=-' * 19)
n2 = int(input('Em que número eu pensei?: ')) # Jogador insere um valor.
print('PROCESSANDO...')
sleep(3)
if n1 == n2:
    print('Você acertou! Parabéns!')
else:
    print('Você escolheu o número {}, e eu o número {}. Tente denovo!'.format(n2, n1))
print('-=-' * 19)