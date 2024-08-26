times = ['Real Madrid', 'Milan', 'Liverpool', 'Bayern de Munique', 'Barcelona']

#a
print(times[0:3])

#b
print(times[3:])

#c
timesOrdenados = sorted(times) #cria nova lista
print(timesOrdenados)

#times.sort() #modifica a lista original
#print(times)

#d
barcelona = times.index('Barcelona')
print(f'O Barcelona está na posição {barcelona + 1}')