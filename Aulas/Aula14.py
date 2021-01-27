"""Laços de repetição - Estrutura WHILE: Aula 14
==================================================
Estrutura de repetição com teste lógigo = While
Estrutura de repetição com váriavel de controle = For
==================================================
Exemplo:
enquanto não maça
    passo
pega
==================================================
Exemplo python:
while não maça:
    passo
pega
==================================================
Exemplo:
enquanto não maça
    se chão
        passo
    se nãochão
        pula
    se moeda
        pega
pega
==================================================
Exemlo python:
while not maça:
    if chão
        passo
    if não chão
        pula
    if moeda
        pega
pega
===================================================
"""

"""Prática"""

'''for c in range(1, 10):
    print(c)
print('FIM')'''

'''
c = 1
while c < 10:
    print(c)
    c += 1
print('FIM')
'''
'''
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM')
'''
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite umm valor: '))
    if n != 0:
        if n % 2 == 0:
            par = + 1
        else:
            impar += 1
print('Você digitou {} números pares e {} números impares.'.format(par, impar))
