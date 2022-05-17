#erro pouco do raciocínio estava correto. problemas com a escrita do programa
valores=[]
c=0
while True:
    n=int(input('Digite um valor: '))

    if n not in valores:
        valores.append(n)
    else:
        print('Número duplicado!')

    cho=str(input('deseja continuar [S/N]?')).upper()
    if cho == 'N':
        break


print(valores)