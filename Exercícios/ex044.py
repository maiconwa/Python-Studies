"""Desafio 044:
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição
de pagamento:
- À vista dinheito/cheque: 10% de desconto.
- À vista no cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- Em 3x ou mais no cartão: 20% de juros"""
print('-=-' * 14)
print('================== LOJA ==================')
print('-=-' * 14)
produto = float(input('Qual é o valor do produto? R$ '))
print('-=-' * 14)
print('Digite a forma de pagamento conforme abaixo: ')
print('-=-' * 14)
print('''[1] para à vista dinheiro/cheque
[2] para à vista no cartão'
[3] para parcelamento em até 2x no cartão
[4] para parcelamento em mais de 3x no cartão''')
print('-=-' * 14)
pagamento = int(input('Digite a opção desejada conforme descrito acima: '))
if pagamento == 1:
    desconto = (produto * 10) / 100
    valorf = produto - desconto
    print('O valor do produto é R$ {:.2f}, com desconto de 10% o valor a ser pago é R$ {:.2f}'.format(produto, valorf))
    print('O valor do desconto foi de R$ {:.2f}'.format(desconto))
elif pagamento == 2:
    desconto = (produto * 5) / 100
    valorf = produto - desconto
    print('O valor do produto é R$ {:.2f}, com desconto de 05% o valor a ser pago é R$ {:.2f}'.format(produto, valorf))
    print('O valor do desconto foi de R$ {:.2f}'.format(desconto))
elif pagamento == 3:
    parcelamento = produto / 2
    print('O valor a ser pago no parcelamento em 2 vezes é R$ {:.2f}'.format(produto))
    print('O valor de cada parcela é R$ {}'.format(parcelamento))
elif pagamento == 4:
    parcelamento = float(input('Em quantas vezes o produto será parcelado? '))
    juros = (produto * 30) / 100
    valorf = juros + produto
    print('O parcelamento foi de {:.0f} vezes no cartão. O juros é R$ {:.2f}'.format(parcelamento, juros))
    print('O valor total a ser pago é R$ {:.2f}'.format(valorf))
else:
    print('-=-' * 14)
    print('Digite uma das oções de [1] a [4].')
print('===FIM===' * 5)
