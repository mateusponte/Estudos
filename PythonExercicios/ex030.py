d=float(input('Olá, digite a distância de sua viagem em km! '))
if d<=200:
    p=float(d*0.50)
    print('O preço da sua viagem é: R${:.2f}'.format(p))
else:
    p=float(d*0.45)
    print('O preço da sua viagem é: R${:.2f}'.format(p))
