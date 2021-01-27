"""Desafio 061:
Refaça o desafio 051, lendo o primeiro termo e a razão da PA, mostrando os 10 primeiros termos da progressão
usando a estrutura while."""

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{} '.format(c), end='-> ')
print('ACABOU')
