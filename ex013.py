salario = float(input('Qual é o seu salário? '))
aumento = float(input('O aumento é de quanto? '))
aumento2 = (salario*aumento)/100
salario2 = salario + aumento2
print('O salário digitado foi {}. O aumento foi de {}. O novo salário é {}'.format(salario, aumento2, salario2))
