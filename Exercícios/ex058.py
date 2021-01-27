"""Desafio 058:
Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador
vai tentar adivinhar até acertar , mostrando no final quantos palpites foram necessários para vencer."""

from random import randint
from time import sleep
# Faz o computador "PENSAR"
computador = randint(0, 10)
jogador = 0
print('-=-' * 20)
print('Vou pensar em número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
while computador != jogador:
    # Jogador tenta adivinhar
    jogador = int(input('Em que número eu pensei? '))
    print('Processando...')
    sleep(1)
    if jogador != computador:
        print('Não foi dessa vez, tente novamente.')
    if jogador == str or jogador == float:
        print('Digite um número inteiro de 0 a 10. Letras, números não inteiros ou simbolos não serão aceitos no jogo ')
print('-=-' * 20)
print('Parabéns! Você conseguiu me vencer!')
print('-=-' * 20)
