# == DESAFIO 022 ==
# Crie um programa que leia o nome completo de uma pessoa e mostre:
''''O nome com todas as letras maiúsculas
O nome com todas minúsculas
Quantas letras ao todo (sem considerar espaços)
Quantas letras tem o primeiro nome'''

nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando o nome "{}"...'.format(nome))
print('Em maiúsculas é {}.'.format(nome.upper()))
print('Em minúsculas é {}.'.format(nome.lower()))
print('Ao todo, o seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))

