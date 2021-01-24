p1 = float(input('Qual é o preço do produto? R$ '))
d1 = (5 * p1)/100
p2 = p1 - d1
print('O preço do produto é R$ {}.'.format(p1))
print('O desconto para este produto é de R$ {}'.format(d1))
print('O seu novo preço é R$ {}'.format(p2))
