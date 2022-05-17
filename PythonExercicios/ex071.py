#caixa eletronico inspirado no ex022 esse é dos bons - FAZER
#sem usar o while você imprime só uma única vez, usar o while para manter o loop
while True:

    valor=int(input('digite o valor a ser sacado: '))


    #quantidade das cédulas de 50
    n1=(valor//50)
    #quantidade das cédulas de 20
    n2=((valor%50)//20)
    #quantidade das cédulas de 10
    n3=(((valor%50)%20)//10)
    #quantidade das cédulas de 1 real
    n4=((((valor%50)%20)%10)//1)

    total = n1*50+n2*20+n3*10+n4*1
    print(f'a quantidade de células de R$50 são {n1}'
          f'\naquantidade de cédulas de R$20 são {n2}'
          f'\na quantidade de cédulas de R$10 são {n3}'
          f'\na quantidade de cédulas de R$1 são {n4}'
          f'\nVocê pediu pra sacar R${total}')
    opç=str(input('deseja continuar? ')).strip().upper()

    if opç == 'N':

        break