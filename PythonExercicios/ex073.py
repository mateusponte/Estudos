#lista de classificados do CBF
times=('Flamengo','Internacional','Atlético-MG','Sâo Paulo','Fluminense','Grêmio','Palmeiras',
       'Santos','Athletico-PR','Bragantino','Ceará SC','Corinthians','Atlético-GO','Bahia','Sport Recife',
       'Fortaleza','Vasco da Gama','Goiás','Coritiba','Botafogo')
for c in range (0,5):

    print(f'O {c+1}° colocado é: {times[c]}\n')
comp=len(times)
for n in range (comp,16,-1):

    print(f'O {n}° colocado é: {times[n-1]}\n')

print(sorted(times))
#Como não tem chapecoense nos times ele não irá ler
#print(times.index('Chapecoense'))
