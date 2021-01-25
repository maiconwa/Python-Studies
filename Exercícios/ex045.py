"""Desafio 045:
Crie um programa que faça o computador jogar Jokenpô com você.
- Pedra ganha de tesoura.
- Papel ganha de pedra
- Tesoura ganha de papel."""

from random import randint
print('-+=+-'*20)
print('VAMOS JOGAR JOKENPÔ:')
print('-+=+-'*20)
print('Escolha conforme abaixo: ')
print('-+=+-'*20)
print('Digite 1 para pedra: ')
print('Digite 2 para papel: ')
print('Digite 3 para tesoura: ')
print('-+=+-'*20)
escolha = int(input('Digite aqui: '))
print('-+=+-'*20)
computador = randint(1, 3)
if escolha == 1 and computador == 3 or escolha == 2 and computador == 1 or escolha == 3 and computador == 2:
    print('Você conseguiu me vencer. Parabéns!')
    print('-+=+-' * 20)
elif computador == 1 and escolha == 3 or computador == 2 and escolha == 1 or computador == 3 and escolha == 2:
    print('Eu venci! Mais sorte na próxima vez.')
    print('-+=+-' * 20)
elif computador == escolha:
    print('Empatamos, temos de jogar novamente outra hora.')
