"""Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores."""

from datetime import date
atual = int(date.today().year)
pessoasn = 0
pessoasv = 0
for c in range(0, 7):
    ano = int(input('Em que ano você nasceu: '))
    idade = atual - ano
    if 18 > idade:
        pessoasn += 1
    else:
        pessoasv += 1
print('No total {} pessoas são menores de idade e {} pessoas são maiores de idade.'.format(pessoasn, pessoasv))
