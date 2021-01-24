from math import radians, sin, cos, tan
angulo = float(input('Digite o valor do angulo: '))
print('O valor do seno é {:.2}'.format(sin(radians(angulo))))
print('O valor do cosseno é {:.2f}'.format(cos(radians(angulo))))
print('O valor da tangente é {:.2f}'.format(tan(radians(angulo))))
