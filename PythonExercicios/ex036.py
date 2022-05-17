print('\033[01;37;41m Olá, seja bem ao programa de crédito\n\033[m')
casa=float(input('digite o valor da sua casa: '))
sal=float(input('digite o valor do seu salário: '))
prazo=float(input('digite o praazo em meses que você deseja pagar: '))

parcela=casa/prazo
if parcela>0.3*sal:
    print('seu crédito não pode ser aprovado, valor da parcela excede 30% do seu salário')
else:
    print('o valor da sua parcela será de R$ {}'.format(parcela))
