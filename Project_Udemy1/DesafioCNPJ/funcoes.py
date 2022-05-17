def validar_cnpj(cnpj):
    novo_cnpj = []
    for num in cnpj:
        if num == "-":
            break
        elif num == "." or num == "/":
            novo_cnpj += ""
        else:
            novo_cnpj += num
    return novo_cnpj


def penul_digito(novo_cnpj):
    cnpj2 = []
    iter = 5
    soma = 0
    for num in novo_cnpj:
        if iter == 1:
            iter = 9
            cnpj2 += str(iter)
            soma = soma + (int(num) * iter)
            iter -= 1
            pass
        else:
            cnpj2 += str(iter)
            soma = soma + (int(num) * iter)
            iter -= 1
    resul = 11 - (soma % 11)

    if resul > 9:
        resul = 0

    return resul


def ult_digito(novo_cnpj):
    cnpj3 = []
    iter = 6
    soma = 0
    for num in novo_cnpj:
        if iter == 1:
            iter = 9
            cnpj3 += str(iter)
            iter -= 1
            soma = soma + (int(num) * iter)
            pass
        else:
            cnpj3 += str(iter)
            soma = soma + (int(num) * iter)
            iter -= 1
    resul = 11 - (soma % 11)

    if resul > 9:
        resul = 0

    return resul
