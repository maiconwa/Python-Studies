"""Desafio 60:
Faça um programa que leia um número qualquer e mostre o seu fatorial.

Exemplo: 5; = 5x4x3x2x1 = 120

com enquanto e for"""

num1 = int(input('Digite um número a ser fatorado: '))
num2 = 0
while num2 > 1:
    print(num2, 'X')
    num2 = num1 - 1
