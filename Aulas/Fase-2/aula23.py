# Introdução ao Try / except
# try -> tentar executar o codigo 
# except -> ocorreu um erro ao tentar executar 

numero_str = input('Vou dobrar o numero que vc digitar: ')

try:
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2}')

except:
    print('Isso não é um numero')
    
    