# == DESAFIO 008 ==
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valor = float(input('Insira um valor em metros: '))
cm = valor * 100
mm = valor * 1000
km = valor / 1000
hm = valor / 100
dam = valor / 10
dm = valor * 10
print('Essa medida de {} metros corresponde a'.format(valor))
print('{:.0f} centímetros\n{:.0f} milímetros\n{:.3f} kilômetros\n{:.2f} hectômetros\n{:.1f} decâmetros\n{} decímetros'.format(cm, mm, km, hm, dam, dm))
