from random import random
#random geral, randint é só numero int randint(0,10) forma de usar
#função max(numeros) e min(numeros) calcula o maior e o menor

numeros=(random(),random(),random(),random(),random())
print(numeros)
print(sorted(numeros))
maior=numeros[0]
menor=numeros[0]
n=len(numeros)


for c in range (0,len(numeros)):

    if maior<numeros[c]:

        maior=numeros[c]

    elif menor>numeros[c]:

        menor=numeros[c]
print(f'o maior número é: {maior}\n')
print(f'o menor número é: {menor}\n')
print(max(numeros))
print(min(numeros))