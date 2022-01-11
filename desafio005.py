# == DESAFIO 5 ==
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
"""
n = int(input('Digite um número: '))
print('O número que digitou é {}. Seu antecessor é o número {} e o seu sucessor é o {}.'.format(n, n - 1, n +1))
"""
print('\033[31m=-\033[m' * 30)
n = int(input('Digite um número inteiro: '))
print('Você digitou o número {}{}{}. O seu sucessor é o {}{}{} e seu antecessor é o {}{}{}.'.format('\033[4;32m', n, '\033[m', '\033[4;32m', n + 1, '\033[m', '\033[4;32m', n - 1, '\033[m'))
print('\033[31m=-\033[m' * 30)