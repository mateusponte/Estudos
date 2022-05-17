#Usando lista e calculando máx e mín
valores=list()
for c in range (0,5):
    valores.append(int(input('Digite um valor: ')))
max=valores[0]
min=valores[0]
pos1=0
pos2=0
for v,f in enumerate(valores):

    if max<f:
        max=f
        pos1=v+1


    if min>f:
        min=f
        pos2=v+1

print(f'O maior valor é {max} na posição {pos1} e o menor é {min} na posição {pos2}')