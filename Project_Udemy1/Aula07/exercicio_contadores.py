contador1=0
contador2=10

while True:
    contador1 += 1
    contador2 -= 1
    print(contador1, contador2)
    if contador1 >=10:
        break


#-------------------------------------------------- código do professor
#r é o valor no range de 10 a 1 e p é o índice do laço. relacionado  ao enumerate
for p, r in enumerate(range(10,1,-1)):
    print(p,r)