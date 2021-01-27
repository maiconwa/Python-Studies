"""Desafio 60:
Faça um programa que leia um número qualquer e mostre o seu fatorial.

Exemplo: 5; = 5x4x3x2x1 = 120

com enquanto e for"""

num2 = 0
num1 = int(input('Digite um número a ser fatorado: '))
acumulador = 0
while num1 > 1:
    print(num1, 'X ', num2)
    if num1 >= 1:
        acumulador = num1 * num1
    num2 = num1 - 1
print(acumulador)