# == DESAFIO 029
'''Escreva um programa que leia a velociodade de um carro. Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada km acima do limite.'''
print('>=' * 10, 'RADAR ELETRÔNICO', '>=' * 10)
limite = 80
velocidade = float(input('A velocidade atual é de... '))
if velocidade > 80:
    multa = (velocidade - limite) * 7
    print('Você está acima do limite de velocidade! Foi aplicado uma multa de R${}!'.format(multa))
print('Tenha um bom dia e dirija com segurança!')
print('>=' * 29)
