#usar o f strings
c=0
s=0
while True:
    n=int(input('Digite um número: '))
    if n==999:
        break
    c+=1
    s+=n
print(f'foram digitados {c} números e a soma entre eles é {s}')