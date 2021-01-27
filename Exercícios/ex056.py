"""Desafio 056:
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
- A média de idade do grupo.
- Qual é o homem mais velho.
- Quantas mulheres têm menos de 20 anos."""

from datetime import date
ano = date.today().year
atual = 0
grupo = 0
media = 0
homemvelho = 0
homemmaisvelho = 0
mulheres = 0
sexo = 0
idade = 0
for c in range(1, 5):
    atual = int(input('Em que ano a {}ª pessoa nasceu: '.format(c)))
    idade = ano - atual
    sexo = int(input('Qual é o sexo da {}ª pessoa? [ 1 ] Masculino [ 2 ] Feminino: '.format(c)))
    media += idade
    grupo += 1
    if sexo == 1 and idade > homemvelho:
        homemvelho = idade
        homemmaisvelho = c
    elif sexo == 2 and mulheres < 20:
        mulheres += 1
    else:
        print('Digite [ 1 ] ou [ 2 ] na escolha do sexo, do contrário não será possivel concluir o programa.')
print('A média de idade de todo o grupo é {}.'.format(media / grupo))
print('O homem mais velho é o {}ª a sua idade é {}.'.format(homemmaisvelho, homemvelho))
print('No total {} mulheres tem menos de 20 anos.'.format(mulheres))
