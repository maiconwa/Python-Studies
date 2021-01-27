"""Desafio 053:
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Ex: APOS A SOPA
Ex: A SACADA DA CASA
Ex: A TORRE DA DERROTA
Ex: O LOBO AMA O BOLO
Ex: ANOTARAM A DATA DA MARATONA"""

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
tudojunto = ''.join(palavras)
inverso = tudojunto[::-1]
'''for letra in range(len(tudojunto) - 1, - 1, - 1):
    inverso += tudojunto[letra]'''
print('O inverso de {} é {}'.format(tudojunto, inverso))
if tudojunto == inverso:
    print('A frase é um palindromo.')
else:
    print('A frase não é um palindromo.')
