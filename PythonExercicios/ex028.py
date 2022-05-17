vel=float(input('Qual a sua velocidade?: '))
if vel<=80:
    print('Você não foi multado!')
else:
    valor=float((vel-80)*7.00)
    print('O valor da sua multa é de: {}'.format(valor))
