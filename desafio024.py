# == DESAFIO 024 ==
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome “SANTO”.

cidade = str(input('Em que cidade você nasceu?: ')).strip()
print('Esta cidade começa com "Santo"?: ', cidade[0:5].upper() == 'SANTO')
