# introdução ao for 

nome =  'Demetrios'
novo_texto = ''

for i in nome: # para cada letra em nome 
    novo_texto += f'*{i}'
    print(i) # exiba a letra 
print(novo_texto + '*')