lista1='012345678901234567890123456789012345678901234567890123456789'
n=10
lista2=[lista1[i:i+n] for i in range(0, len(lista1), n)]
comb='.'.join(lista2)
print(comb)