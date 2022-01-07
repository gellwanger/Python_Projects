def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False
    erros = 6

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = str(input("Qual letra? ").strip().upper())

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros -= 1
            print("Ops, você errou! Faltam {} tentativas.".format(erros))

        enforcou = erros == 0
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você acertou!!")
    else:
        print("Você perdeu")
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()