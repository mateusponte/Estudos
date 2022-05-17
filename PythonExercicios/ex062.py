a1=int(input('Digite o primeiro termo da PA: '))
raz=int(input('Digite a razão: '))
s=int(input('Você quer quantos termos? '))
c=1
an=0

x=0
while s!=0:
    an=a1+c*raz
    print('O {}° termo da PA é: {}'.format(c,an))
    c+=1
    x+=1
    if x==s:
        s=int(input('Você quer mostrar mais quantos termos? '))
        x=0