"""
Formatação basica de strings
s - string 
d - int 
f - float
<número de dígito>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel:-^10}')
print(f'{1000.123456789:,.1f}')
print(f'O hexadecimal de 2000 é {2000:08x}') # hexadecimal em minusculo 
print(f'O hexadecimal de 2000 é {2000:08X}') # hexadecimal em maiusculo
