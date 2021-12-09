# == DESAFIO 026 ==
# Faça um programa que leia uma frase pelo teclado e mostre:
# -	Quantas vezes aparece a letra “A”.
# -	Em que posição ela aparece a primeira vez.
# -	Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase;'.format(frase.count('A')))
print('A primeira ocorrência da letra A é na {}ª posição;'.format(frase.find('A') + 1))
print('A última ocorrência da letra A é na {}ª posição.'.format(frase.rfind('A') + 1))

# é possível mudar a posição inicial de 0 para 1 simplesmente somando o número 1