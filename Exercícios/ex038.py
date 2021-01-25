"""Desafio 038:
Escreva um programa que leia dois números inteiros e compare-os. Mostrando na tela uma mensagem:
- O primeiro valor é maior.
- O segundo valor é maior
- Não existe valor maior, os dois são iguais"""

num1 = int(input('Digite um o primeiro número inteiro: '))
num2 = int(input('Digite um o segundo número inteiro: '))

if num1 > num2:
    print('O primeiro valor, número {} é maior que o número {}.'.format(num1, num2))
elif num1 < num2:
    print('O segundo valor, número {} é maior que o número {}.'.format(num2, num1))
else:
    print('Não exite valor maior. O primeiro número {} é igual ao segundo número {}.'.format(num1, num2))
