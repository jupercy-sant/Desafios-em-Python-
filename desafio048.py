# DESAFIO 048
# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
cont = 0
for numero in range(1, 501, 2):
    if numero % 3 == 0:
        cont = cont + 1
        soma = numero + soma
print('A soma de todos os {} números é igual a {}.'.format(cont, soma))
