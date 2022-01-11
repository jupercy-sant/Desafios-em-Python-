# == DESAFIO 002 ==
# Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

""""
print('Olá. Qual é a sua data de nascimento?')
dia = input('Dia = ')
mes = input('Mês = ')
ano = input('Ano = ')
print('Você nasceu no dia', dia, 'de', mes, 'de', ano, ', Correto?')
"""

print('\033[1;32m>=\033[m' * 20)
print('Olá! Qual é a sua data de nascimento?')
d = int(input('Dia = '))
m = int(input('Mês = '))
a = int(input('Ano = '))
print('Você nasceu no dia {}{}{}, do mês {}{}{} do ano {}{}{}, correto?'.format('\033[4;35m', d, '\033[m', '\033[4;35m', m, '\033[m', '\033[4;35m', a, '\033[m'))