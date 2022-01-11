# == DESAFIO 001 ==
# Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado.
"""
nome = input('Bem-vindo(a)!Qual é o seu nome?')
print('Bem-vindo(a)',nome,'!')
"""

print('\033[0;31m=-\033[m' * 20)
nome = input('Olá. Qual é o seu nome? ')
if nome == 'Jupercy':
    print('Que nome {}dahora{}!'.format('\033[1;32m', '\033[m'))
else:
    print('Seu nome poderia ser mais {}dahora{}... Mas de boa!'.format('\033[1;32m', '\033[m'))
print('Olá, {}{}{}! Tenha um bom dia!'.format('\033[1;32m', nome, '\033[m'))
print('\033[0;31m=-\033[m' * 20)
