# == DESAFIO 5 ==
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número: '))
print('O número que digitou é {}. Seu antecessor é o número {} e o seu sucessor é o {}.'.format(n, n - 1, n +1))