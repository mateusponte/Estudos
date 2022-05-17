lista_de_lista_de_inteiros = [[1,2,3,4,5,6,7,8,9,10],[9,1,8,9,9,7,2,1,6,8]]


def encontra_primeiro_duplicado(para_lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1
    for numero in para_lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break

        numeros_checados.add(numero)

    return primeiro_duplicado


for lista_de_inteiros in lista_de_lista_de_inteiros:
    print(lista_de_inteiros, encontra_primeiro_duplicado(lista_de_inteiros))




