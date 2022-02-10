import random

def jogar():
    imprime_mensagem_inicial()

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    imprime_mensagem_escolha_dificuldade()

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou " , chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            imprime_mensagem_erro_escopo()
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            imprime_mensagem_acerto(pontos)            
            break
        else:
            if(maior):
                imprime_mensagem_erro_maior()
                
            elif(menor):
                imprime_mensagem_erro_menor()
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")

# Funções:
def imprime_mensagem_inicial():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

def imprime_mensagem_erro_escopo():
    print("Você deve digitar um número entre 1 e 100!")

def imprime_mensagem_escolha_dificuldade():
    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

def imprime_mensagem_acerto(pontos):
    print("Você acertou e fez {} pontos!".format(pontos))

def imprime_mensagem_erro_maior():
    print("Você errou! O seu chute foi maior do que o número secreto.")
def imprime_mensagem_erro_menor():
    print("Você errou! O seu chute foi menor do que o número secreto.")

if(__name__ == "__main__"):
    jogar()
