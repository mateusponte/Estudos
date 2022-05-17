expre=str(input('Digite um expressão: '))
list=[]
for simb in expre:
    if simb == '(':
        list.append('(')
    elif simb == ')':
        if len(list)>0:
            list.pop()
        else:
            list.append(')')
            break
if len(list)==0:
    print('Sua expressão é válida')
else:
    print('Sua expressão não é válida')
