# DESAFIO 057
# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe o seu sexo: [M/F] ')).strip().upper()[0] #Pega o sexo da pessoa, joga pra maiúsculo, remove espaços e apenas o primeiro caractere
while sexo not in 'MmFm':
    sexo = str(input('Dados inválidos. Por favor, informe o seu sexo: ')).strip().upper()[0]
print('Sexo {} informado com sucesso'.format(sexo))