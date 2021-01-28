"""Desafio 60:
Faça um programa que leia um número qualquer e mostre o seu fatorial.

Exemplo: 5; = 5x4x3x2x1 = 120

com enquanto e for"""


num1 = int(input('Digite um número a ser fatorado: '))
num2 = num1 - 1
f = 0
while num2 < num1:
    print(num1 * (num1 - f))
    f += 1
    num2 -= 1
    num1 -= 1
