n1=float(input('digite sua primeira nota: '))
n2=float(input('digite sua segunda nota: '))
media=(n1+n2)/2

if media>=7:
    print('Você está aprovado!')
elif media>=5 and media<=6.9:
    print('você está de recuperação!')
elif media<5:
    print('Você está reprovado! Estude mais!')