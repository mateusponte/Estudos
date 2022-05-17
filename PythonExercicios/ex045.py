#jokenpô
from random import choice
print('Esse é um programa pra jogar jokenpô!')

jogador=str(input('escolhe sua mão: '))

jogador = jogador.upper()
lista=['PEDRA','PAPEL','TESOURA']
maquina=choice(lista)
print('Máquina escolheu {}'.format(maquina))

if maquina=='PEDRA' and jogador =='TESOURA':
    print('você perdeu!')
elif maquina=='PAPEL' and jogador=='PEDRA':
    print('você perdeu!')
elif maquina=='TESOURA' and jogador=='PAPEL':
    print('você perdeu!')
elif jogador=='PEDRA' and maquina =='TESOURA':
    print('você ganhou!')
elif jogador=='PAPEL' and maquina=='PEDRA':
    print('você ganhou!')
elif jogador=='TESOURA' and maquina=='PAPEL':
    print('você ganhou!')
elif jogador == maquina:
    print('empate!')