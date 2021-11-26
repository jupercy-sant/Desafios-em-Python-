# == DESAFIO 014 ==
# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

c = float(input('Digite a temperatura atual em celsius: '))
f = ((9 * c) / 5) + 32
print('A temperatura de {} Cº equivale a {} Fº.'.format(c, f))

