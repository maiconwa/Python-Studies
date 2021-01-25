"""Desafio 042:
Refaça o desafio 035 dos triângulos, acressentando o recurso de mostrar que tipo de triangulo será formado.
- Equilátero: todos os lados iguais
- Isóceles: Dois lados iguais
- Escaleno: Todos os lados são diferentes"""

print('-=-' * 20)
print('Analisador de Triângulos 2.0')
print('-=-' * 20)
a = float(input('Digite o valor do promeiro segmento: '))
b = float(input('Digite o valor do segundo segmento: '))
c = float(input('Digite o valor do terceiro segmento: '))
if (b - c) < a < (b + c) and (a - c) < b < (a + c) and (a - b) < c < (a + b):
    print('Os segmentos acima podem formar um triângulo!')
    if a == b == c:
        print('O triângulo que será formado é um triângulo EQUILÁTERO, pois todos os lados são iguais.')
    elif a == b != c or a == c != b or b == a != c:
        print('O triangulo que será formado é um triângulo ISÓCELES, pois apenas dois lados são iguais')
    else:
        print('O triângulo que será formado é um triângulo ESCALENO, pois todos os lados são diferentes')
else:
    print('Não é possivel formar um triângulo')
