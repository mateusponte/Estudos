#lista de preços
produtos=('Lápis','Borracha','Caderno','Estojo','Transferidor',
          'Compasso', 'Mochila', 'Caneta', 'Livro',
          34.90, 22.30, 120.30, 9.99, 4.20, 25.00, 15.90, 2.00, 1.75)
t=18
z=9
m=t-1
for c in range(0, z):

    print(f'{produtos[c]}','.'*20,f'R${produtos[m]:.2f}')
    m-=1