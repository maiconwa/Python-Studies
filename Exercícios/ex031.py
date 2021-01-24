dis = float(input('Qual é a distância da viagem? '))
if dis <= 200:
    print('O valor total da passagem é de R${}'.format(dis * .5))
else:
    print('O valor total da passagem é de R${}'.format(dis * .45))
