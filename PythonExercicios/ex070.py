#cadastro de caixa de supermercado
total=0
MaisM=0
barato=''
barpre=50000000000000000
while True:

    nome=str(input('Digite o nome do produto: ')).strip().upper()
    preço=float(input('Digite o preço do produto: '))


    total+=preço

    if preço>1000:

        MaisM+=1

    elif preço<barpre:

        barpre=preço
        barato=nome

    escol=str(input('deseja continuar [S/N]: ')).strip().upper()

    if escol=='N':
        break


print(f'O total de produtos é {total}\n Produtos acima de R$1000,00 foram {MaisM}\n O produto mais barato foi {barato} custando {barpre:.2f}')
