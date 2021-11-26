# == DESAFIO 010 ==
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$5.46

real = float(input('Insira o valor de conversão em reais. R$'))
dol = real / 5.46
euro = real / 6.31
libra = real / 7.37
print('Com R${:.2f}, você pode comprar US$ {:.2f}, EUR¢ {:.2f} ou GBP {:.2f}. \nSó chora com esse dóla kkkkj'.format(real, dol, euro, libra))
