""" Desafio 037:
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão"""

numero = int(input('Digite um numero inteiro a ser convertido: '))
conversao = int(input("Digite 1 para binário, 2 para octal e 3 para hexadecimal: "))

if conversao == 1:
    convertido = bin(numero)
    print('A conversão do numero {} para binário é {}'.format(numero, convertido))
elif conversao == 2:
    convertido = oct(numero)
    print('A conversão do número {} para octal é {}'.format(numero, convertido))
elif conversao == 3:
    convertido = hex(numero)
    print('A conversão do número {} para hexadecimal é {}'.format(numero, convertido))
