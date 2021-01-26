"""Fase 13: Curso de Python - Laços de repetição (Parte 1)
====================================================================
Laço de variavel de controle = Laço de iteração = Laço de repetição:
####################################################################
Exemplo:
laço c no intervalo(1, 10)
    passo
pega
####################################################################
Python:
for c in range(1, 10):
    passo
pega
####################################################################
Exemplo:
laço c no intervalo(0, 3)
    passo
    pula
passo
pega
####################################################################
Python:
for c in range(0, 3):
    passo
    pula
passo
pega
####################################################################
Exemplo:
laço c no intervalo(0, 3)
    se moeda
        pega
    passo
    pula
passo
pega
####################################################################
Python:
for c in range(0, 3):
    if moeda
        pega
    passo
    pula
passo
pega
####################################################################
"""

"""Prática:"""
"""
i = int(input('início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')
"""
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print('O somatório de todos os valores foi {}'.format(s))
