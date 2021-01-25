""" Desafio 037:
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão"""

numero = int(input('Digite um numero inteiro a ser convertido: '))
print('''Escolha uma das opções abaixo: 
print('[1] Converter para BINÁRIO.
print('[2] Converter para OCTAL.
print('[3] Converter para HEXADECIMAL.''')
conversao = int(input("Digite a sua opção: "))
if conversao == 1:
    print('A conversão do numero {} para binário é {}'.format(numero, bin(numero)[2:]))
elif conversao == 2:
    print('A conversão do número {} para octal é {}'.format(numero, oct(numero)[2:]))
elif conversao == 3:
    print('A conversão do número {} para hexadecimal é {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção invalida. Tente novamente.')
