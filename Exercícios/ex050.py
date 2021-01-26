"""Desafio 50:
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for impar desconsidere-o"""

par = 0
soma = 0
cont = 0
for c in range(1, 7):
    par = int(input('Digite o {}º numero inteiro par: '.format(c)))
    if par % 2 == 0:
        soma += par
        cont += 1
    else:
        print('Valores impares serão desconsiderados.')
print('A soma dos valores digitados é {} e você informou {} números pares.'.format(soma, cont))
