import random

def jogar():
    imprime_mensagem_bemvindo()

    numero_secreto = random.randrange(1, 101)
    pontos = 1000
    nivel = escolha_do_nivel()

    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1, total_tentativas + 1):
        print("Tentativas {} de {}".format(rodada,total_tentativas))
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou", chute)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        if (numero_secreto == chute):
            imprime_mensagem_vencedor(pontos)
            break
        else:
            if (chute > numero_secreto):
                print("Você errou! Seu número foi maior que o número secreto")
                if (rodada == total_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            elif (chute < numero_secreto):
                print("Você errou! Seu número foi menor que o número secreto")
                if (rodada == total_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do Jogo!")


def imprime_mensagem_bemvindo():
    print("*************************************")
    print("**Bem vindo ao jogo de Adivinhação!**")
    print("*************************************")

def escolha_do_nivel():
    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))
    return nivel

def imprime_mensagem_vencedor(pontos):
    print("Você acertou e fez {} pontos".format(pontos))
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

if(__name__ == "__main__"):
    jogar()
