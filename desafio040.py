# == DESAFIO 040 ==
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: Reprovado
# - Média entre 5.0 e 6.9: Recuperação
# - Média 7.0 ou superior: Aprovado

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Sua primeira nota é {} e a segunda nota é {}. Sua média é {}'.format(n1, n2, media))
if media < 5:
    print('Infelizmente você foi reprovado. Estude mais.'.format(media))
# elif media >= 5 and media < 7: Usando operadores lógicos
elif 7 > media >= 5: # Jeito tradicional da matemática.
    print('Você está de RECUPERAÇÃO. Se esforce mais.'.format(media))
elif media >= 7:
    print('Você foi APROVADO.'.format(media))