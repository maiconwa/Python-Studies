"""Desafio 39:
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar n serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date
ano = int(date.today().year)
nascimento = int(input('Digite o ano em que você nasceu: '))
idade = ano - nascimento
if idade > 18:
    alistamento = idade - 18
    print('Você tem {} anos, seu periodo de alistamento já passou faz {} anos.'.format(idade, alistamento))
    data = ano - alistamento
    print('Seu alistamento foi em {}'.format(data))
elif idade < 18:
    alistamento = 18 - idade
    print('Você tem {} anos, lembre-se que você ainda irá se alistar em {} anos.'.format(idade, alistamento))
    data = ano - alistamento
    print('Seu alistamento será em {}'.format(data))
elif idade == 18:
    print('Você tem {} anos. Chegou a hora de se alistar.'.format(idade))
