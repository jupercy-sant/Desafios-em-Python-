# == DESAFIO 003 ==
# Crie um script Python que leia dois números e tente mostrar a soma entre eles.
"""
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print('A soma entre {} e {} é igual a {}!'.format(n1, n2, n1 + n2))
"""

print('\033[1;36m=-\033[m' * 20)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print('A soma desses dois número é igual a {}{}{}.'.format('\033[1;33m', s, '\033[m'))
print('\033[1;36m=-\033[m' * 20)