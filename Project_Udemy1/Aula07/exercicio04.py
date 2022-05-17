nome=str(input('Olá, digite seu nome: '))

if len(nome)<=4:
    print('Seu nome é curto!')
elif len(nome)>4 and len(nome)<=6:
    print('Seu nome é normal!')
elif len(nome)>6:
    print('Seu nome é muito grande!')

