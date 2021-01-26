"""Desafio 50:
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for impar desconsidere-o"""

par = 0
soma = 0
for c in range(0, 6):
    par = int(input('Digite um número inteiro par: '))
    if par % 2 == 0:
        soma += par
    else:
        print('Valores impares serão desconsiderados.')
print('A soma dos valores digitados é {}.'.format(soma))
