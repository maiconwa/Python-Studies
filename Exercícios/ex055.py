"""Desafio 055:
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos. """
peso = 0
menor = 0
maior = 0
for c in range(0, 5):
    peso = int(input('Digite o peso de uma pessoa: '))
    if peso > maior:
        maior = peso
        if menor == 0:
            menor = peso
    elif menor < peso:
        menor = peso
print('O maior peso digitado foi {}Kg e o menor foi {}Kg.'.format(maior, menor))
