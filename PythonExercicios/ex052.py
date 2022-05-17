#número primo
n=int(input('digite um número: '))
soma=0
for c in range(1,n+1,1):
    if n%c==0:
        soma+=c
if soma!=n+1:
    print('o número não é primo')
else:
    print('o número é primo')

