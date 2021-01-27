"""Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores."""

from datetime import date
atual = date.today().year
pessoasn = 0
pessoasv = 0
for c in range(1, 8):
    ano = int(input('Em que ano a {}º pessoa nasceu: '.format(c)))
    idade = atual - ano
    if 21 >= idade:
        pessoasn += 1
    else:
        pessoasv += 1
print('No total {} pessoas são menores de idade e {} pessoas são maiores de idade.'.format(pessoasn, pessoasv))
