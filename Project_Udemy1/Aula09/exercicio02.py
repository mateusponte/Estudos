l1 = [1,2,3,4,5,6]
l2=[1,2,3,4,5,6]
total=[]
if len(l1) > len(l2):
    for c in range(len(l2)):
        total.append(l1[c] + l2[c])
else:
    for c in range(len(l1)):
        total.append(l1[c] + l2[c])

print(total) #existe a forma do professor, verificar depois