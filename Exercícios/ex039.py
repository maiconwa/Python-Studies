"""Desafio 39:
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar n serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date
nascimento = int(input('Digite o ano em que você nasceu: '))
ano = int(date.today().year)

if ano - nascimento > int(18):
    print('Você tem {} anos, seu periodo de alistamento já passou.'.format(ano - nascimento))
elif ano - nascimento < int(18):
    restante = 18 - (ano - nascimento)
    print('Você tem {} anos, lembre-se que você ainda irá se alistar em {} anos.'.format(ano - nascimento, restante))
elif ano - nascimento == int(18):
    print('Você tem {} anos. Chegou a hora de se alistar.'.format(ano - nascimento))
