#par ou ímpar
from random import choice
vit=0
print('bem vindo ao programa para jogar par ou ímpar')
while True:
    jogador=str(input('Escollha PAR/ÍMPAR: ')).strip().upper()
    jognum=int(input('Escolhe um número de 0 a 10: '))
    num=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    comp=choice(num)
    if jogador=='IMPAR':
        soma=jognum+comp
        if soma%2 == 0:
            print('Você perdeu!')
            break
        elif soma%2 !=0:
            print('Você ganhou!')
    elif jogador == 'PAR':
        soma=jognum+comp
        if soma%2 == 0:
            print('Você ganhou!')
        elif soma%2 != 0:
            print('Você perdeu!')
            break
    vit+=1

print(f'você ganhou {vit} vezes')