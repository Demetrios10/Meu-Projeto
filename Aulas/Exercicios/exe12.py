# Calculadora com while

while True:
    numero1 = input('Digite primeiro numero: ')
    numero2 = input('Digite segundo numero: ')
    operador = input('Digite um dos Operadores (+ - * /): ')
    
    numeoros_validos = None
    num_1_float = 0
    num_2_float = 0
    
    try:
        num_1_float = float(numero1)
        num_2_float = float(numero2)
        numeoros_validos = True
    except:
        numeoros_validos = None

    if numeoros_validos is None:
     print('Um ou ambos os numeros digitados são invalidos. ')
     continue
    
    operadores_permitidos = '+ - * /'
    
    if operador not in operadores_permitidos:
        print('Operador invalido. ')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um Operador. ')
        continue
    if operador == '+':
        print(f'{num_1_float}+{num_2_float} =' , num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float}-{num_2_float} =' , num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float}/{num_2_float} =' , num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float}*{num_2_float} =' , num_1_float * num_2_float)
         
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        print('vc saiu!!')
        break
    
    
    
    
    
    
    
    