#fazer ambos os exercícios 76-77 bons exercícios
#bom método, entender essa funcionalidade do python que não há no c,c++
#ver e aprender novos comandos
palavras=('Abacate','Laranja','Tomate','Maça','Abacaxi','Banana','Pera','Coco')


for p in palavras:
    print(f'\nNa palavra {p} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='')
