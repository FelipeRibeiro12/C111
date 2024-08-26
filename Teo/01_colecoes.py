#COLECOES

# Tuplas: ()/ imutavel/ visao de viwer "nao pode ser alterado", 

#nomes = ('Goku', 'Vegeta', 'Trunks', 'Gohan')

#select
#print(nomes)
#print(nomes[0])
#print(nomes[1:3]) #! slicing - [i:j] / i = inclusive / j = exclusive / ignorando Goku e Gohan

#insert, update, delete
#nomes[0] = 'Picolo' ! tupla e um objeto imutavel

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Listas: []/ mutavel/ visao de editor "pode ser alterado"

#nomes = ['Goku', 'Vegeta', 'Trunks', 'Gohan']

#select
#print(nomes[2:]) #slicing

#insert
#nomes.insert(0, 'Picolo') #adiciona por meio de indice e valor
#nomes.append('Kuririn') #adiciona no final da lista

#update
#nomes[0] = 'Bulma'

#delete
#nomes.remove('Gohan') #remove por meio do valor
#del nomes[1] #remove por meio do indice

#['Bulma', 'Goku', 'Vegeta', 'Trunks', 'Gohan', 'Kuririn']

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Conjuntos: {}/ nao guarda a ordem dos elementos, nao tem indices/ mutavel/ nao guarda repeticoes "duplicatas"/ guardar dados unicos "cpf, email,..."

#nomes = {'Goku', 'Vegeta', 'Trunks', 'Gohan'}

#select
#print(nomes)

#insert
#nomes.add('Bulma')
#nomes.add('Goku') #! nao aceita valores duplicados

#!update: remover um elemtento e adicionar outro

#delete
#nomes.remove('Vegeta')

#{'Goku', 'Vegeta', 'Gohan', 'Trunks'}

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Dicionarios: {}/ mutavel/ chave:valor/ nao guarda a ordem dos elementos

#pessoa = {'nome': 'Goku',
#          'idade': 40,
#          'sexo': 'm'
#} #! chave:valor

#select
#print(pessoa['idade'])

#insert
#pessoa['hobbie'] = 'comer'

#update
#pessoa['nome'] = 'Gohan'

#delete
#del pessoa['sexo']

#{'nome': 'Gohan', 'idade': 40, 'hobbie': 'comer'}