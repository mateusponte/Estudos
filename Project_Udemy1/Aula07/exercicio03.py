hora = input('Olá, digite a hora: ')
if hora.isdigit():
    if float(hora)>=0 and float(hora)<=11:
        print('Bom dia!')
    elif float(hora)>=12 and float(hora)<=17:
        print('Boa tarde!')
    elif float(hora)>=18 and float(hora)<=23:
        print('Boa noite!')
    elif float(hora)>23:
        print('Não é um valor de hora entre 0-23')
else:
    print('Não é um valor de hora!')