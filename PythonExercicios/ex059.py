s=9
while s!=5:
    n1=int(input('digite um número: '))
    n2=int(input('digite um número: '))
    s=int(input('Você deseja \n[1]Somar os valores'
                '\n[2]Multiplicar'
                '\n[3]Maior'
                '\n[4]Novos valores'
                '\n[5]sair do programa:\n '))
    if s==1:
        print('A soma dos valores é: {}'.format(n1+n2))
    elif s==2:
        print('A multiplicação dos valores é: {}'.format(n1*n2))
    elif s==3:
        if n1>n2:
            print('O maior é: {}'.format(n1))
        elif n2>n1:
            print('O maior é: {}'.format(n2))
