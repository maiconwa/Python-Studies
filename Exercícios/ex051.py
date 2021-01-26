"""Desafio 51:
Desenvolva um programa que leia o primeiro termo e a razao de uma PA. No final mostre os 10 primeiros termos dessa
progressão. """

lista = []
valor = 0
for c in range(0, 10):
    valor = str(input('Digite um número de 0 a 9: '))
    lista += valor
print(lista)
