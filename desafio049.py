# == DESAFIO 049 ==
# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print('{}{:=^40}{}'.format('\033[2;32m', ' TABUADAS ', '\033[m'))
multi = int(input('Digite um número para saber sua tabuada: '))
for num in range(1, 11):
    print('{} X {} = {}'.format(multi, num, multi * num))
print('{}{:=^40}{}'.format('\033[2;32m', ' FIM ', '\033[m'))
