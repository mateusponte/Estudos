frase=str(input('digite uma frase: ')).strip()
n=len(frase)
n2=len(frase)
soma=0

for c in range (0,n+1,1):
    if frase[c] == frase[n2]:
      soma+=1
    n2-=1

if soma==n:
    print('A frase é um palíndramo!')
else:
    print('A frase não é um palíndramo!')