print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
a = float(input('Digite o valor do promeiro segmento: '))
b = float(input('Digite o valor do segundo segmento: '))
c = float(input('Digite o valor do terceiro segmento: '))
if (b - c) < a < (b + c) or (a - c) < b < (a + c) or (a - b) < c < (a + b):
    print('Os segmentos acima podem formar um triângulo!')
else:
    print('Não é possivel formar um triângulo')
