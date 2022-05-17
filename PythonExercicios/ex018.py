import random
from random import choice
n1=str(input('Digite o nome do aluno: '))
n2=str(input('Digite o nome do aluno: '))
n3=str(input('Digite o nome do aluno: '))
n4=str(input('Digite o nome do aluno: '))
lista=[n1, n2, n3, n4]

print('O aluno escolhido é: {}'.format(choice(lista)))
print('O aluno escolhido é: {}'.format(random.choice(lista)))