cpf=input('Digite seu cpf: ')

val_cpf = ''
novo_cpf = ''
for caractere in cpf:
    if caractere == '.' or caractere == '-':
        val_cpf += ''
    else:
        val_cpf += caractere

soma = 0
contador = 10
for j in range(0, 10):

    soma = soma + int(val_cpf[j])*contador
    contador -=1


digito1 = (11 - (soma % 11))
print(digito1)

for i in range(0, 9):
    novo_cpf += str(val_cpf[i])
    print(val_cpf[i])
if digito1>9:
    novo_cpf = novo_cpf + '0'
soma2= 0
contador2= 11
for k in range(0, len(novo_cpf)):

    soma2 = soma2 + (int(novo_cpf[k])*contador2)
    contador2 -= 1

digito2 = 11 - (soma2 % 11)

novo_cpf = novo_cpf + str(digito2)

print(f'{novo_cpf}')

if novo_cpf == val_cpf:
    print(f'Seu cpf {cpf} é válido')
else:
    print(f'Seu cpf {cpf} não é válido')
"""
print(f'{val_cpf}')
print(f'{soma} \n {11 - (soma % 11)}')
"""