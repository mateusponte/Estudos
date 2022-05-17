matriz=[[],[],[]]
for c in range (0,3):
    for p in range (0,3):
        n=int(input(f'digite o elemento {c}{p} número: '))
        matriz[c].append(n) #outra opção seria usr matriz[c][p]=int(input(f'Digite um número'))

print(f'{matriz[0]} \n {matriz[1]} \n {matriz[2]}')