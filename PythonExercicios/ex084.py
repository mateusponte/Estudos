cadastro=list()
cad1=list()
cad2=list()
pessoa=0
mp=0
ml=0
while True:
    cadastro.append(str(input('digite seu nome: ')))
    cadastro.append(int(input('digite seu peso: ')))
    pessoa+=1
    cho=str(input('Deseja continuar: ')).strip()
    if cho in 'Nn':
        break
mp=cadastro[0][1]
ml=cadastro[0][1]
for p in cadastro:
    if p[1] > mp:
        mp == p[1]
    elif p[1] < ml:
        ml == p[1]
for c in cadastro:
    if c[1] == mp:
        cad1.append(cadastro[c])
    elif c[1] == ml:
        cad2.append(cadastro[c])

print(f'Foram cadastradas {pessoa} pessoas')
print(f'Mais pesada {cad1} \n Mais leve {cad2}')
