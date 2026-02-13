# adivinhando as letras que não estão na palavra

palavra = input("Digite uma palavra: ")
letra_dentro_do_palavra = input('Digite uma letra que deseja encontrar na palavra: ')


if letra_dentro_do_palavra not in palavra:
    print(f'a letra {letra_dentro_do_palavra} digitada não esta na palavra !!')
else:
    print(f'a letra {letra_dentro_do_palavra} digitada esta na palavra !')
    
    