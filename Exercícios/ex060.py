"""Desafio 60:
Faça um programa que leia um número qualquer e mostre o seu fatorial.

Exemplo: 5; = 5x4x3x2x1 = 120

com enquanto e for"""

'''
numero = int(input("Fatorial de: "))
resultado = 1
count = 1

while count <= numero:
    resultado *= count
    count += 1

print(resultado)
'''
numero = int(input("Fatorial de: "))
resultado = 1
count = 1
for count in range(0, numero):
    resultado *= count

print(resultado)
