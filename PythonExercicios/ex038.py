n1=float(input('digite um número: '))
n2=float(input('digite outro número: '))

if n1>n2:
    print('O valor {} é maior que o valor {}'.format(n1,n2))
elif n2>n1:
    print('O valor {} é maior que o valor {}'.format(n2,n1))
else:
    print('Os valores {} e {} são iguais'.format(n1,n2))