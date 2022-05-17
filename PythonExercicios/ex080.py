#lista sem usar o sort bom exercício pensar mais antes // reduzir o ritmo e treinar mais
#insight olhar o funcionamento, usar outro for dentro da for maior para verificar os números e depois alocá-lo
#copia=valores[:]
valores= []

for c in range (0,5):
    n=int(input('Digite um número: '))
    if c == 0 or n>valores[-1]: #n>valores[len(valores)-1]: #n>valores[-1]
        valores.append(n)
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)
                break
            pos +=1



print(valores)






