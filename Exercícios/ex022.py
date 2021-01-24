nome = input(str('Digite o seu nome completo: '))

print(nome.upper())
print(nome.lower())
print(nome.strip())

nome1 = nome.split()
print(nome1[0])

print(len(nome1[0][1:]))
