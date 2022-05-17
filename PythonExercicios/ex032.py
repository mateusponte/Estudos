#com erro e refazer
n1=int(input('digite um número: '))
n2=int(input('digite um número: '))
n3=int(input('digite um número: '))

if  n1>n2 and n1<n3:
    print('O maior número é {}'.format(n1))
elif n1>n2 and n1<n3:
    print('O maior número é {}'.format(n3))
elif n3>n1 and n3<n2:
    print('O maior número é {}'.format(n2))
elif n2>n1 and n1>n3:
    print('O maior número é {}'.format(n2))

