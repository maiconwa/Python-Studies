"""Desafio 043:
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo
com a tabela abaixo:
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- Entre 25 e 30: Sobrepeso
- Entre 30 e 40: Obesidade
- Acima de 40: Obesidade mórbida"""

peso = float(input('Digite o seu peso: (Kg) '))
altura = float(input('Digite a sua altura: (m) '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('O seu peso é {}Kg, sua altura é {}m, o IMC é {:.1f}, abaixo do peso.'.format(peso, altura, imc))
elif 18.5 <= imc < 25:
    print('O seu peso é {}Kg, sua altura é {}m, o IMC é {:.1f}, peso ideal.'.format(peso, altura, imc))
elif 25 <= imc < 30:
    print('O seu peso é {}Kg, sua altura é {}m, o IMC é {:.1f}, sobrepeso.'.format(peso, altura, imc))
elif 30 <= imc < 40:
    print('O seu peso é {}Kg, sua altura é {}m, o IMC é {:.1f}, obesidade.'.format(peso, altura, imc))
elif 40 < imc:
    print('O seu peso é {}Kg, sua altura é {}m, o IMC é {:.1f}, obsidade mórbida. CUIDADO!'.format(peso, altura, imc))
