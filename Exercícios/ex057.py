"""Desafio 057:
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto. """

'''
sexo = ''
cont = 0
while cont == 0:
    sexo = str(input('Digite o sexo da pessoa, [ M ] Masculino [ F ] Feminino: ')).strip().upper()
    if sexo != 'M' and sexo != 'F':
        print('Digite [ M ] para masculino e [ F ] para feminino, outras respostas não são validas.')
    else:
        cont += 1
if sexo == 'M':
    print('O Sexo da pessoa digitado é {}.'.format('Masculino'))
else:
    print('O sexo da pessoa digitado é {}.'.format('Feminino'))
'''

'''Correção:'''
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Digite uma opção valida. Informe seu sexo: [M/F] ')).strip().upper()[0]
print('O sexo informado é {}'.format(sexo))
