dis = float(input('Qual é a distância da viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(dis))
if dis <= 200:
    print('O valor total da passagem é de R${:.2f}'.format(dis * .5))
else:
    print('O valor total da passagem é de R${:.2f}'.format(dis * .45))
print('Boa viagem!')
