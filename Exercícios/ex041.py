"""Desafio 041:
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
categoria, de acordo com a idade.
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 20 anos: SÊNIOR
- Acima de 20 anos: MASTER"""

from datetime import date
nascimento = int(input('Digite o ano de nascimento do atleta: '))
ano = int(date.today().year)
classificacao = ano - nascimento
if classificacao <= 9:
    print('A categoria para este atleta que tem {} anos é a MIRIM.'.format(classificacao))
elif 9 < classificacao <= 14:
    print('A categoria para este atleta que tem {} anos é a INFANTIL.'.format(classificacao))
elif 14 < classificacao <= 19:
    print('A categoria para este atleta que tem {} anos é a JÚNIOR.'.format(classificacao))
elif 19 < classificacao <= 20:
    print('A categoria para este atleta que tem {} anos é a SÊNIOR'.format(classificacao))
elif classificacao > 20:
    print('A categoria para este atleta que tem {} anos é a MASTER'.format(classificacao))
