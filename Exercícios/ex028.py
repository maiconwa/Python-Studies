from random import randint
from time import sleep
# Faz o computador "PENSAR"
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
# Jogador tenta adivinhar
jogador = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(3)
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no número {}!'.format(computador, jogador))
