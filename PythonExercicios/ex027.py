from random import choice
#from random import randint

n=[0, 1, 2, 3, 4, 5]
f=int(input('Olá, digite um número inteiro de 0 a 5: '))
z=choice(n)

if f==z:
    print('Parabéns, você acertou!')
else:
    print('Você errou, tente novamente')
#z=randint(0, 5) outra forma de fazer