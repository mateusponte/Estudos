#fatorial
n1=int(input('digite um número: '))
n2=n1
fat=1
while n2!=0:
   fat=fat*n2
   n2-=1

print('O fatorial de {} é: {}'.format(n1,fat))