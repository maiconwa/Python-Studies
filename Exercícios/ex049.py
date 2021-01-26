"""Desafio 049:
Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for """

tabuada = int(input('Digite o valor que quer ver na tabuada: '))
tamanho = int(input('Digite o tamanho da tabuada requerida: '))
print('-' * 13)
for c in range(0, tamanho+1):
    print('{} x {:3} = {}'.format(tabuada, c, (c * tamanho)))
print('-' * 13)
print('FIM')
print('-' * 13)
