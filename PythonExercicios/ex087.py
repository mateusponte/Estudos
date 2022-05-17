matriz=[[],[],[]]
soma=0
soma3=0
max=0

for c in range (0,3):
    for p in range (0,3):
        n=int(input(f'digite o elemento {c}{p} número: '))
        matriz[c].append(n)
        if n%2==0:
            soma+=n


        if p == 2:
            soma3+=n
        if c==1:
            if n>max:
                max=n


print(f'{matriz[0]} \n {matriz[1]} \n {matriz[2]}')
print(f'A soma de todos os valores pares é {soma} \n A soma dos elementos da terceira coluna é {soma3}\n e o maior valor da segunda linha é {max}')