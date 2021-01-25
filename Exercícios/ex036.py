""" Desafio 36:
    Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa, O programa vai perguntar o valor
da casa, o salário do comprador e em quantos anos ele vai pagar.
    Calcule o valor da prestação mensal, sabendo que ela nao pode exceder 30% do salário ou então o empréstimo será
negado. """

casa = float(input('Qual é o valor do imóvel? '))
salario = float(input('Qual é o valor do salário? '))
tempo = float(input('Em quantos anos o imóvel será pago? '))
prestacao = casa / (tempo * 12)
if prestacao <= (salario * .3):
    print('O valor da prestação é de R${:.2f}. Está em 30% do seu salário R${:.2f}.'.format(prestacao, salario))
    print('O empréstimo será realizado. Tenha um bom dia!')
elif prestacao > (salario * .3):
    print('O valor da prestação é de R${:.2f}. Está acima de 30% do seu salário R${:.2f}.'.format(prestacao, salario))
    print('O empréstimo não será realizado. Tenha um bom dia!')
