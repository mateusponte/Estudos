list=[]
list1=[]
list2=[]
while True:
    n=int(input('Digite um número: '))
    list.append(n)
    if n%2 == 0:
        list2.append(n)
    else:
        list1.append(n)
    cho=str(input('Deseja continuar [S/N]?')).upper().strip()

    if cho == 'N':
        break

print(f'Os valores digitados foram {list} \n Os números ímpares são {list1}\n Os números pares são {list2}')
