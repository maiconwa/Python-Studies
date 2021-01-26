"""Desafio 046:
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 até 0,
com uma pausa se 1 segundo entre eles."""

from time import sleep
print('=-' * 23)
print('CONTAGEM REGRESSIVA PARA OS FOGOS DE ARTIFICIO')
print('=-' * 23)
for c in range(10, 0, -1):
    sleep(1)
    print(c)
print('=-' * 23)
print('FELIZ ANO NOVO!!!')
print('=-' * 23)