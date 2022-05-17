list=[]
q=0
while True:
    n=int(input('Digite um número: '))
    list.append(n)
    q+=1
    cho=str(input('Deseja continuar [S/N]?')).strip().upper()
    if cho == 'N':
        break
list.sort(reverse=True)
print(f'Foram digitados {q} números \n A lista em ordem decrescente é {list}')
if 5 in list:
    print('\nO valor 5 está na lista')
else:
    print('O valor 5 não foi digitado')