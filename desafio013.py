# == DESAFIO 013 ==
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salário do funcionário Epaminondas: '))
aumento = salario + (salario * 15 / 100)
print('O salário de R${:.2f} com aumento de 15% será R${:.2f}'.format(salario, aumento))
