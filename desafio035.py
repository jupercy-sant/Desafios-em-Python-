# == DESAFIO 035 ==
"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""

print(">=" * 15)
print('|PODE FORMAR UM TRIÂNGULO?|')
print("<=" * 15)
v1 = float(input('Digite a primeira medida: '))
v2 = float(input('Digite a segunda medida: '))
v3 = float(input('Digite a terceira medida: '))
if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v1 + v2:
    print('Os segmentos acima PODEM formar um triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo!')

