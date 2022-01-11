"""
== DESAFIO 046 ==
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
com uma pausa de 1 segundo entre eles.
"""
import emoji
from time import sleep
print('Que comece a contagem regressiva!')
sleep(2)
conf = str(input('Digite S/N para iniciar a contagem regressiva! '))
if conf == 's':
    for cont in range(10, -1, -1):
        print('{}!'.format(cont))
        sleep(1)
    print(emoji.emojize('FELIZ ANO NOVO! :sparkles: :boom: :smile:', use_aliases=True))
else:
    print('Até a próxima!')
