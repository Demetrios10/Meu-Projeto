# Introdução a f-strings
#
# f-string: prefixo f antes das aspas; variáveis e expressões vão entre { }.
# Mais legível que concatenar com + e str().

nome = "Demetrios"
sobrenome = "Alves da Silva"
altura = 1.80000
cidade = "São Paulo"
rua = "Nora Ney"

strings = 'nome: {} \nsobrenome: {} \naltura: {:.2f} \ncidade: {} \nrua: {} '.format(nome , sobrenome , altura , cidade , rua)
print(strings)


