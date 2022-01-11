from random import randint
computador = randint(0, 10)
print('=-' * 20)
print('{:=^40}'.format(' JOGO DE ADIVINHAÇÃO '))
print('=-' * 20)
print('Vamos jogar um jogo? Estou pensando em um número entre 0 e 10, tente adivinhar...')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Continue tentando!')
        elif jogador > computador:
            print('Menos... Continue tentando!')
print('Acertou! Número de tentativas: {}'.format(palpites))
