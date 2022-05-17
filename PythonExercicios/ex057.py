#ler o sexo da peça
sexo=str(input('digite o seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo=str(input('Valor inválido. Digite novamente: ')).strip().upper()[0]
print('Obrigado')