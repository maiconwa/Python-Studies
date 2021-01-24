salario = float(input('Qual é o salário do funcionário? R$'))
if salario > 1250:
    print('O novo salário é de {}'.format(salario+(salario*.1)))
else:
    print(('O novo salário é de {}'.format(salario+(salario*.15))))
