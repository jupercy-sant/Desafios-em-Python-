# == DESAFIO 052 ==
# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

numero = int(input('Digite um número inteiro: '))
total = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print('\033[31m', end=' ')
        total += 1
    else:
        print('\033[32m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divisível {} vezes.'.format(numero, total))
if total == 2:
    print('O número {} é um número PRIMO.'.format(numero))
else:
    print('O número {} NÃO é um número PRIMO.'.format(numero))
