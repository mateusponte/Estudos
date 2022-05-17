carrinho = []
while True:
    produto = str(input('Digite o produto: '))
    preco = float(input('Digite o preço: '))



    carrinho.append((produto,preco))
    choice=str(input('Deseja continuar comprando [s/n]: '))

    if choice == 'n':
        break

    else:
        print(f'Seu carrinho: {carrinho}')



print(f'Total é: {sum([y for x,y in carrinho])}')