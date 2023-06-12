#jogo palavra secreta

import os

palavra_secreta = input('Digite uma palabra secreta para começar a bricadeira: ').lower()

os.system('cls')
print('Jogo Palavra Secreta\nTente adivinhar a palabra digitando uma letra de cada vez\n')
letras_acertadas = ''
numero_tentativas = 0
while True:
    
    letra_digitada = input('Digite uma letra: ').lower()
    numero_tentativas += 1
    
    if len(letra_digitada) > 1:
        print ('digite apenas uma letra')
        continue

    if letra_digitada == '0' :
        break

    if  letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''

    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print('Palavra formada: ',palavra_formada,'\n')

    
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print( 'VOCÊ GANHOU!!!')
        print('A palavra era: ', palavra_secreta)
        
        print('Número de tentativas: ', numero_tentativas)
        break
    




