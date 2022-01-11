# Desafio 042
# Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

v1 = float(input('Digite a primeira medida: '))
v2 = float(input('Digite a segunda medida: '))
v3 = float(input('Digite a terceira medida: '))
if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v1 + v2:
    print('Os seguimentos acima PODEM formar um triângulo ', end='')
#   if v1 == v2 and v2 == v3: Primeira forma
    if v1 == v2 == v3: #Segunda forma (ambos funcionam)
        print('EQUILÁTERO.')
    elif v1 != v2 != v3 != v1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('Os seguimentos acima NÃO PODEM formar um triângulo.')