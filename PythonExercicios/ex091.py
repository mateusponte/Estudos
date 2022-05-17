#criar um programa onde 4 jogadores jogam um dado e tenham resultados aleatórios. Guarde os resultados em um dicionário.
#No final coloque os dados em ordem sabendo que o vencendor tirou o maior número no dado
#tem que ver o vídeo do exercício
from random import choice
import time
dado=[0, 1, 2, 3, 4, 5, 6]
resultado=[]
jog1={choice(dado)}
print(f'O jogador1 tirou {jog1}')
time.sleep(1)
jog2={choice(dado)}
print(f'O jogador2 tirou {jog2}')
time.sleep(1)
jog3={choice(dado)}
print(f'O jogador3 tirou {jog3}')
time.sleep(1)
jog4={choice(dado)}
print(f'O jogador4 tirou {jog4}')
time.sleep(1)
resultado.append(jog1)
resultado.append(jog2)
resultado.append(jog3)
resultado.append(jog4)

print(resultado)
