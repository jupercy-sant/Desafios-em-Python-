# == DESAFIO 011 ==
'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².'''

print('Este é um programa que calcula a área de uma parede e verifica quanto de tinta será necessário para pintar.')
lar = float(input('Quanto de largura tem a parede? '))
alt = float(input('Quanto de altura tem a parede? '))
área = lar * alt
tinta = área / 2
print('Uma parede com dimensão {} X {} possui {}m².'.format(lar,alt, área))
print('Para pintar essa parede, será necessário aproximadamente {} litros de tinta'.format(tinta))
