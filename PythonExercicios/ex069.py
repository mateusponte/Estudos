#cadastro de pessoas
id=0
M=0
F=0
mid=0
while True:
    idade=int(input('Digite sua idade: '))
    sexo=str(input('Digite seu sexo [M/F]: ')).strip().upper()
    while sexo not in 'MF':
        sexo=str(input('Digite seu sexo [M/F]: ')).strip().upper()

    if idade>18:
        mid+=1
    elif sexo =='F' and idade<20:
        F+=1
    elif sexo=='M':
        M+=1
    resp=str(input('deseja continuar [s/n]: ' )).strip().upper()
    if resp =='N':
        break
print(f'A quantidade de mulheres menores que 20 são {F} \n A quantidade de pessoas maiores que 18 são {mid} \nA quantidade de homens cadastrados são {M}')