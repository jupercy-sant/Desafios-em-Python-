# DESAFIO 045
# Crie um programa que faça o computador jogar jokenpô com você
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções: 
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Sua jogada: '))
print('JO...')
sleep(1)
print('KEN...')
sleep(1)
print('PO!!!')
sleep(1)
print('=-' * 12)
print('O computador jogou {}'.format(itens[computador]))
print('O jogador jogou {}'.format(itens[jogador]))
print('=-' * 12)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Jogador VENCEU!')
    elif jogador == 2:
        print('Computador VENCEU!')
    else:
        print('Jogada INVÁLIDA!')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('Computador VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Jogador VENCEU!')
    else:
        print('Jogada INVÁLIDA')
elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('Jogador VENCEU!')
    elif jogador == 1:
        print('Computador VENCEU!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada INVÁLIDA')
