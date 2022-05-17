n1=int(input('digite um número: '))
n2=int(input('digite um número: '))
n3=int(input('digite um número: '))

if n1+n2>n3 and n2+n3>n1 and n1+n3>n2:
    print('As retas formam um triângulo!')
else:
    print('As retas não formam um triângulo!')