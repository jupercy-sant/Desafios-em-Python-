# == DESAFIO 043 ==
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

from math import pow
peso = float(input('Digite o seu peso: (Kg) '))
altura = float(input('Digite a sua altura: (m) '))
imc = peso / (pow(altura, 2))
print('O seu IMC é {:.1f}.'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal.')
elif imc >= 25 and imc < 30:
    print('Você está em sobrepeso.')
elif imc >= 30 and imc < 40:
    print('Você está obeso.')
elif imc >= 40:
    print('Você está em obesidade mórbida.')
