# == DESAFIO 044 ==
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/ cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

print('{:+^40}'.format(' LOJAS LOJÍSTICAS '))
preço = float(input('Digite o preço do produto: R$'))
print('''FORMAS DE PAGAMENTO 
[1] À VISTA no DINHEIRO/ CHEQUE
[2] À VISTA no CARTÃO
[3] 2x no CARTÃO
[4] 3x ou mais no CARTÃO''')
pagamento = int(input('Selecione uma das opções: '))
if pagamento == 1:
    desconto = preço - (preço * 10 / 100)
elif pagamento == 2:
    desconto = preço - (preço * 5 / 100)
elif pagamento == 3:
    parcela = preço / 2
    desconto = preço
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(preço))
elif pagamento == 4:
    vezes = int(input('Digite o número de vezes: '))
    parcela = preço / vezes
    desconto = preço + (preço * 20 / 100)
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(vezes, parcela))
else:
    desconto = preço
    print('Opção INVÁLIDA. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, desconto))
