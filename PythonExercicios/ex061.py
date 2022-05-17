#PA com While
a1=int(input('Digite o primeiro termo da PA: '))
raz=int(input('Digite a razão: '))
c=1
an=0
while c!=11:
    an=a1+c*raz
    print('O {}° termo da PA é: {}'.format(c,an))
    c+=1