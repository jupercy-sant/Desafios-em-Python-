# == DESAFIO 050 ==
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

print('Digite 6 números inteiros: ')
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('{}º número: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você digitou {} números PARES e a soma entre eles é igual a {}.'.format(cont, soma))


