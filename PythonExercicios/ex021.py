nome=str(input('Digite seu nome: ')).strip() #remove os espaços no início e no fim
print(nome.upper())
print(nome.lower())
dividido=nome.split()
print('O primeiro nome tem {} letras'.format(nome.find(' ')))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('Seu nome tem ao todo {} letras'.format(len(dividido[0])))