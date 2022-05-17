#somatório dos números multiplos de 3 // não precisava o cálculo só usar a função resto ANIMAL
soma2=0
for c in range(1,501,1):
    unid= c//1 % 10
    dez = c//10 % 10
    cen= c//100 % 10
    soma1=(unid+dez+cen)
    if soma1%3==0:
        soma2 += c
        print(c)
print(soma2)