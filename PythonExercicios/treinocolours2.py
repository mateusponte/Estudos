nome=str(input('Olá, digite seu nome! ')).strip()
colour={'Preto':'\033[7:30m'}
print('{}Seja bem vindo {}{}, \nEste é nosso programa de coresS!'.format(colour['Preto'], nome, '\033[m'))