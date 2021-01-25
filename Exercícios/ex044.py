"""Desafio 044:
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição
de pagamento:
- À vista dinheito/cheque: 10% de desconto.
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- Em 3x ou mais no cartão: 20% de juros"""

produto = float(input('Qual é o valor do produto? '))
print('-=-' * 20)
print('Digite a forma de pagamento conforme abaixo: ')
print('-=-' * 20)
print('Digite 1, para à vista dinheiro/cheque')
print('Digite 2, para à vista no cartão')
print('Digite 3, para parcelamento em até 2x no cartão')
print('Digite 4, para parcelamento em mais de 3x no cartão')
print('-=-' * 20)
pagamento = float(input('Digite a opção desejada conforme descrito acima: '))
if pagamento == 1:
    valorf = (produto * .10) + produto
    print('O valor do produto é {:.2f}, com desconto de 10% o valor a ser pago é {:.2f}'.format(produto, valorf))
elif pagamento == 2:
    valorf = (produto * .05) + produto
    print('O valor do produto é {:.2f}, com desconto de 05% o valor a ser pago é {:.2f}'.format(produto, valorf))
elif pagamento == 3:
    print('O valor a ser pago no parcelamento em 2 vezes é {:.2f}'.format(produto))
elif pagamento == 4:
    parcelamento = float(input('Em quantas vezes o produto será parcelado? '))
    valorf = ((produto * .20) * parcelamento) + produto
    print('O valor a ser pago no parcelamento de {} vezes no cartão é de {}'.format(parcelamento, valorf))
