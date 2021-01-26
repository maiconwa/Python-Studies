"""Desafio 048: Faça um programa que calcule a soma entre todos os números impares que são multiplos de três e que se
encontram no intervalo de 1 até 500. """

soma = 0
cont = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos estes valores é {}, foram somados {} numeros'.format(soma, cont))
