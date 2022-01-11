# == DESAFIO 051 ==
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA (progressão aritmética).
# No final, mostre os 10 primeiros termos dessa progressão aritmética.

print('{:=^40}'.format(' 10 TERMOS DE UMA PA '))
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão # Fórmula do enésimo de uma PA
for c in range(primeiro, décimo + razão, razão): # O enésimo termo soma mais a razão porque o último termo não aparece
    print('{} '.format(c), end=' → ')
print('FIM')
