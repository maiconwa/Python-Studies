velocidade = int(input('Qual a velocidade do carro? '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('Sua velocidade foi de {}Km. Você ultrapassou o limite de 80Km a multa é de R${}'.format(velocidade, multa))
else:
    print('Você respeitou o limite de velocidade. Parabéns!')
print('---FIM---')