
termos=int(input('Digite o numero de termos: '))
an=1
t=0
t1=1
while an!=termos+1:
    ter = t1 + t
    print('O {} termo de fibonacci é {}'.format(an,t)) #se i 0 contar deixa assim, senão trocar t por t1
    t=t1
    t1=ter
    an+=1
