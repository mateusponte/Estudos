#salvar dados numa tupla
#bom exercício
n=(int(input('digite um número: ')),
   int(input('digite um número: ')),
   int(input('digite um número: ')),
   int(input('digite um número: ')))

print(f'O número 9 apareceu {n.count(9)} vezes\n')

if 3 in n:
    print(f'O valor 3 apareceu na {n.index(3)+1}')
else:
    print(f'O valor 3 não aparece na tupla')
print('Os números pares foram: ', end='')
for l in n:
    if l%2==0:
        print(l,end=' ')
        


