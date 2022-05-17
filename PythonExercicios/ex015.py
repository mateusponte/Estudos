#dizer a parte real de um número
from math import trunc
n1=float(input('Digite um número real qualquer: '))
print('A parte inteira de {} é: {}'.format(n1,trunc(n1)))