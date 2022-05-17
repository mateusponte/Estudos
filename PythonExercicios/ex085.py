num=[[],[]]
for c in range (0,7):
    numb=int(input('digite um número: '))
    if numb%2==0:
        num[1].append(numb)
    elif numb%2!=0:
        num[0].append(numb)

num.sort()

print(f'Os números ímpares são {num[0]}\n Os números pares são {num[1]}')