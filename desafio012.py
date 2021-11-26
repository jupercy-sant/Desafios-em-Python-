# == DESAFIO 012 ==
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('Bem-vindo ao catálogo de preços do Super Mercado Cabeça de Ovo!')
produto = input('Digite o nome do produto: ')
preço = float(input('Digite o preço do produto: R$'))
desconto = float(input('Digite quantos porcento de desconto: '))
pcd = preço - (preço * desconto / 100)
print('Com {}% de desconto, o produto {} cai de R${} para R${}! É imperdível!'.format(desconto, produto, preço, pcd))
