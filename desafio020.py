# == DESAFIO 020 ==
# - O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.  Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
aluno1 = str(input('Nome do primeiro aluno: '))
aluno2 = str(input('Nome do segundo aluno: '))
aluno3 = str(input('Nome do terceito aluno: '))
aluno4 = str(input('Nome do quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)