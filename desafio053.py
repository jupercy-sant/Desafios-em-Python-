# == DESAFIO 053 ==
# Crie um programa que leia uma frase qualquer e diga se ela é um palímdromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)

inverso = ''
for letra in range(len(junto) - 1, -1, -1): # Começa em length de "junto", vai até a letra -1 que é antes da primeira, e vai voltando uma letra
    inverso = inverso + junto[letra]

# inverso = junto[::-1] # Nessa opção sem for, a contagem pode ser feita do começo ao fim só que de trás pra frente

print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
    