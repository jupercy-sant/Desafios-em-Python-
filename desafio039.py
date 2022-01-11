# DESAFIO 039
#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.

from datetime import date
anoatual = date.today().year
anonasc = int(input('Digite o ano de nascimento: '))
idade = anoatual - anonasc
print('Quem nasceu em {} tem {} anos em {}.'.format(anonasc, idade, anoatual))
if idade == 18:
    print('Quem nasceu no ano de {} deverá fazer o alistamento IMEDIATAMENTE.'.format(anonasc))
elif idade < 18:
    saldo = 18 - idade
    ano = anoatual + saldo
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    print('Ainda não completou 18 anos. Seu alistamento será em {}.'.format(ano))
elif idade > 18:
    saldo = idade - 18
    ano = anoatual - saldo
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    print('O seu alistamento foi em {}.'.format(ano))
