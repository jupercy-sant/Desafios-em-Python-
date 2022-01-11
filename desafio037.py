# == DESAFIO 037 ==
"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
- 1 para binário
- 2 para octal
- 3 para hexadecimal
"""

print('\033[1;32m', '-.' * 15, '\033[m', '\033[1;33m', ' CONVERSOR ', '\033[m', '\033[1;32m', '-.' * 15, '\033[m')
print('BEM-VINDO ao CONVERSOR de números!')
n = int(input('Digite um número inteiro para converter: '))
print('''Escolha uma das bases para conversão:
Digite [ 1 ] para converter para BINÁRIO
Digite [ 2 ] para converter para OCTAL
Digite [ 3 ] para converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}.'.format(n, bin(n)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}.'.format(n, oct(n)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}.'.format(n, hex(n)[2:]))
else:
    print('Opção INVÁLIDA. Tente novamente!')
