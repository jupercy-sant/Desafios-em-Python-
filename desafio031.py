# == DESAFIO 031 ==
'''Desenvolva um programa que pergunte a distância de uma viagem em km.
Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.'''
distancia = float(input('Qual é a distância da viagem? '))

'''
Método comum:
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45'''

preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('A passagem irá custar R${:.2f}!'.format(preco))
