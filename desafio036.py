# == DESAFIO 036
"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
"""
from time import sleep

print('\033[1;32m=+\033[m' * 15, '\033[4;31mBANCO MANEIRO\033[m', '\033[1;32m+=\033[m' * 15)
resposta = str(input('Bem-vindo ao Banco Maneiro ltda. Estaria interessado em um empréstimo para compra de uma casa? S/N: '))
if resposta == 's':
    print('LOADING...')
    sleep(3)
    valorcasa = float(input('Digite o valor da casa: R$'))
    salário = float(input('Digite o seu salário: R$'))
    anos = int(input('Quantos anos de financiamento: '))
    prestação = valorcasa / (anos * 12)
    mínimo = salário * 30 / 100 # Calcula o mínimo de 30% do salário
    print('Para pagar uma casa de R${:.2f} em {} anos,'.format(valorcasa, anos), end='')
    print('a prestação será de R${:.2f}.'.format(prestação))
    if prestação <= mínimo:
        print('LOADING...')
        sleep(3)
        print('O seu empréstimo foi {}APROVADO{}.'.format('\033[4;33m', '\033[m'))
    else:
        print('Empréstimo {}NEGADO{}!'.format('\033[4;33m', '\033[m'))

else:
    print('Obrigado pela visita! Volte sempre!')