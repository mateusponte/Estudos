lista_de_lista_de_inteiros = [[1,2,3,4,5,6,7,8,9,10],[9,1,8,9,9,7,2,1,6,8]]
  #  lista reduzida

for k in lista_de_lista_de_inteiros:

    for i in range(len(k)):
        n = k[i]
        duplicados = 0
        for j in range(0,len(k)):
            n1 = k[j]

            if j == k:
                break

            if n1 == n:
                duplicados +=1

            else:

                continue

        if duplicados == 0:
            print(f'Não há itens duplicados. {k}')

    if duplicados != 0:
        print(f'Há itens duplicados.')