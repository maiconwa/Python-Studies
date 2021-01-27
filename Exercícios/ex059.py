"""Desafio 059:
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso."""

escolha = ''
resultado = 0
continuar = ''
n1 = 0
n2 = 0
while continuar != 'N':
    n1 = float(input('Informe o primeiro valor: '))
    n2 = float(input('Informe o segundo valor: '))
    print('''    
    Escolha uma das operações abaixo: 
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa    ''')
    escolha = int(input('Digite aqui a sua escolha: '))
    if escolha == 1:
        resultado = n1 + n2
        print('A soma de {} e {} é {}.'.format(n1, n2, resultado))
        continuar = str(input('Deseja fazer outra operação? [ S ] Sim [ N ] ')).strip().upper()
    elif escolha == 2:
        resultado = n1 * n2
        print('A multiplicação de {} e {} é {}.'.format(n1, n2, resultado))
        continuar = str(input('Deseja fazer outra operação? [ S ] Sim [ N ] ')).strip().upper()
    elif escolha == 3:
        if n1 > n2:
            print('{} é maior que {}.'.format(n1, n2))
            continuar = str(input('Deseja fazer outra operação? [ S ] Sim [ N ] Não ')).strip().upper()
        elif n1 == n2:
            print('{} e {} são valores iguais.'.format(n1, n2))
            continuar = str(input('Deseja fazer outra operção? [ S ] Não [ N ] ')).strip().upper()
        else:
            print('{} é maior do que {}.'.format(n2, n1))
            continuar = str(input('Deseja fazer outra operação? [ S ] Sim [ N ] Não ')).strip().upper()
    elif escolha == 4:
        continuar = 'S'
    elif escolha == 5:
        continuar = 'N'
    else:
        print('Por favor digite uma das opções válidas.')
print('======Programa encerrado======')
print('=======Tenha um bom dia=======')
