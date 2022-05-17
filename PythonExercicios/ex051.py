#PA
a1=int(input('digite o primeiro termo da PA: '))
raz=int(input('digite a razão: '))
dec=a1+raz*10
n=1
for c in range(a1,dec,raz):
    print('o {}° termo da progressão é: {}'.format(n,c))
    n=n+1

