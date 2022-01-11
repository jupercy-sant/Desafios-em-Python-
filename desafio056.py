# DESAFIO 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# •	A média de idade do grupo
# •	Qual é o nome do homem mais velho
# •	Quantas mulheres têm menos de 20 anos

somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1,5):
    print('-------- {} PESSOA --------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade # A somaidade recebe ela mesma mais a idade da pessoa
    totmulher20 = 0
    if p == 1 and sexo in 'Mm': #Aqui verifica ambos M maiúsculo e minúsculo
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem: #Se o sexo ainda estiver dentro de masculino e a idade do homem for maior que a maior idade do homem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20: #Aqui é verificado quantas mulheres tem menos de 20 anos
        totmulher20 += 1

médiaidade = somaidade / 4J
print('A média de idade do grupo é de {} anos.'.format(médiaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))
