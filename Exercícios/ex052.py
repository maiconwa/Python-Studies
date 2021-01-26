"""Desafio 052:
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo. """

num = int(input('Digite um número: '))
primo = 0
for c in range(2, num):
    if num % c == 0:
        primo += 1
if primo == 0 and num != 1:
    print('É primo')
else:
    print('O número {} tem {} multiplos acima de 2 e abaixo de {}. Portanto não é primo.'.format(num, primo, num))
