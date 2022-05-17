#tabuada com for
n=int(input('digite o número para calcular a tabuada: '))

for c in range(0, 11):
    tab=n*c
    print('\nO valor de {}x{} é: {}'.format(n,c,tab))