#melhorando um programa
from random import choice
comp=[0,1,2,3,4,5,6,7,8,9,10]
escol=choice(comp)

n=int(input('escolha um número de 0 a 10: '))
pal=1
while n!=escol:
    n=int(input('escolha um número de 0 a 10: '))
    pal+=1
print('Parabéns, você acertou após {} palpites'.format(pal))