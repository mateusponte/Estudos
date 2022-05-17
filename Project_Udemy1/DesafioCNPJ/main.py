from funcoes import validar_cnpj, penul_digito, ult_digito  # 04.252.011/0001-10 40.688.134/0001-61

cnpj = str(input("digite o seu cnpj: "))

novo_cnpj = validar_cnpj(cnpj)
cnpj3 = []
print(novo_cnpj)
# até está tudo funcionando

penul = penul_digito(novo_cnpj)
ultimo = ult_digito(novo_cnpj)

for num in novo_cnpj:
    cnpj3 += str(num)
cnpj3 += str(penul) + str(ultimo)

# falta só criar uma função que com laço verificar número a número
if cnpj3 != cnpj:
    print(f'O cnpj não é válido {cnpj}  / {cnpj3}')
else:
    print(f'O cnpj é válido :{cnpj}')

#  até aqui funcionando

# atenção, quando a lista é passada para funções o retorno dela é diferente de qnd operada dentro do proprio arquivo
# ver forma de corrigir
# tem como usar o código para gerar um cnpj válido
