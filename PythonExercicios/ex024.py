nome=str(input('digite seu nome: ')).strip()
dividido=nome.split()

print('seu primeiro nome é: {}\nseu último nome é: {}'.format(dividido[0] , dividido[len(dividido)-1]))