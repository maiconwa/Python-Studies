# Exemplo 1:
# tempo = int(input('Quantos anos tem o seu carro? '))
# if tempo <= 3:
#     print('Carro novo')
# else:
#     print('Carro Velho')
# print('---FIM---')

# Exemplo 2:
# tempo = int(input('Quantos anos tem o seu carro? '))
# print('Carro novo' if tempo <= 3 else 'Carro velho')
# print('---FIM---')

# Exemplo 3
# nome = str(input('Qual é o seu nome? '))
# if nome == 'Maicon':
#     print('Que nome lindo você tem.')
# else:
#     print('Seu nome é tão normal!')
# print('Bom dia, {}.'.format(nome))

# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a segunda nota: '))
# m = (n1 + n2) / 2
# print('A sua média foi {:.1f}.'.format(m))
# if m >= 6.0:
#     print('Sua média foi boa, parabéns!')
# else:
#     print('Sua média foi ruim, estude mais!')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}.'.format(m))
print('Parabéns!' if m >= 6 else 'Estude mais!')
