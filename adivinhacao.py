import random
import jogos


def mensagem_vitoria(pontuacao):
    if(pontuacao < 30):
        print(f"É preciso melhorar, sua pontuação foi de {pontuacao}.")
    elif(pontuacao < 60):
        print(f"Muito bem!, sua pontuação foi de {pontuacao} pontos!")
    elif(pontuacao < 90):
        print(f"Que incrível!!, sua pontuação foi de {pontuacao} pontos!!")
    else:
        print(f"Perfeito!!!, sua pontuação foi de {pontuacao} pontos!!!")

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


def mensagem_derrota(numero_secreto, pontuacao):
    print("\n")
    print(" XXXXXXX XXXXXXX XXX    XXX XXXXXX   ")
    print(" XX      XX   XX XXXX  XXXX XX       ")
    print(" XX  XXX XXXXXXX XX XXXX XX XXXXXX   ")
    print(" XX   XX XX   XX XX  XX  MM XX       ")
    print(" XXXXXXX XX   XX XX      XX XXXXXX   ")
    print(" \n")
    print(" XXXXXXX XX       XX XXXXXX XXXXXX  ")
    print(" XX   XX  XX     XX  XX     XX  XX  ")
    print(" XX   XX   XX   XX   XXXXXX XXXXXX  ")
    print(" XX   XX    XX XX    XX     XX XX    ")
    print(" XXXXXXX     XXX     XXXXXX XX  XX   ")
    print("\n")

    print(f"O número secreto era {numero_secreto}.\n"
          f"Sua pontuação foi de {pontuacao} pontos, é preciso melhorar muito.")
    print("Obrigado por Jogar!")


def mensagem_inicial():
    print("******************************************")
    print("**** Bem vindo ao Jogo de advinhação! ****")
    print("******************************************\n")

    print("- Regras:\n"
          "* Você terá que acertar um número secreto entre 1 e 100!\n"
          "* Você começa com 100 pontos.\n"
          "* Você perde pontos quanto mais tentativas gasta.\n"
          "* Cada nível te dá uma certa quantidade de tentativas:\n"
          "- Fácil = 20 tentativas.\n"
          "- Médio = 10 tentativas.\n"
          "- Dificíl = 5 tentativas.\n"
          "* Não digite letras,símbolos e não deixe o espaço de resposta vazio.\n"
          " * Bom jogo! *\n")
    print("Qual será o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")  # (4) Impossivel


def play_again():
    escolhido = False
    while (escolhido is False):
        print("Você quer:\n"
              "* (1) Jogar denovo?\n"
              "* (2) Ir para seleção de Jogos?\n"
              "* (3) Parar de Jogar?\n")
        resposta = input("Selecione uma opção: ")
        if(resposta.isnumeric):
            resposta = int(resposta)
            if(resposta == 1):
                print("Preparando Advinhação...\n")
                jogar()
                break
            elif(resposta == 2):
                print("Preparando Sala de Seleção...\n")
                jogos.escolha_seu_jogo()
                break
            elif(resposta == 3):
                print("Finalizando jogo...\n")
                break
        else:
            print("Escolha uma das opções somente e digite apenas números.")


def jogar():

    mensagem_inicial()

    numero_secreto = random.randrange(1, 101)
    total_de_rounds = 3
    round_atual = 1
    pontuacao = 100
    pontos_a_perder = 100
    indice = 1
    tolerancia = 10
    # quantidade_dicas = 3

    for indice in range(1, tolerancia + 1):
        nivel = input("Escolha o nível de dificuldade:")
        if(nivel.isnumeric()):
            nivel_int = int(nivel)
            if(nivel_int == 1):
                total_de_rounds = 20
                pontos_a_perder = 5
                break
            elif(nivel_int == 2):
                total_de_rounds = 10
                pontos_a_perder = 10
                break
            elif(nivel_int == 3):
                total_de_rounds = 5
                pontos_a_perder = 20
                break
            # elif(nivel_int == 4):
            #     total_de_rounds = 1
            #     pontos_a_perder = 25
            #     print("* Você escolheu o nível impossivel, por causa disso você terá 3 dicas.\n"
            #           "* A cada dica usada você perde 1 quarto dos pontos no resultado final, caso você acertar./n"
            #           "* Você só tem uma tentativa, se errar , você perde todos os pontos."
            #           "* Boa sorte , você vai precisar.")
            #
            else:
                print(f"Essa dificuldade não existe!")
                indice += 1
        else:
            print("Digite apenas números!")
            indice += 1

    for round_atual in range(1, total_de_rounds + 1):

        if (indice == tolerancia + 1):
            break

        limite = 10
        permitido = False

        for posicao in range(0, limite):
            print(f"Round {round_atual} de {total_de_rounds}")  # .format(round_atual,total_de_rounds)
            # if(nivel_int == 4):
            #     print(f"Você tem {quantidade_dicas} dica(s)")
            #     print("(1) Sim\n(2) Não")
            #     resposta = input("Quer usar uma dica:")
            #     if(resposta.isnumeric()):
            #         resposta = int(resposta)
            #         if(resposta == 1):

            chute_str = input("Digite o seu número, entre 1 e 100: ")
            print(f"Seu chute é: {chute_str}")
            print(numero_secreto)
            if(chute_str.isnumeric()):
                chute = int(chute_str)
                if (chute > 100):
                    print("Você deve digitar um número entre 1 e 100!")
                else:
                    permitido = True
                    break
            else:
                print("Digite apenas números!\r\n")
                print("Não:\r\n"
                      "- Digite letras e símbolos\r\n"
                      "- Digite números negativos ou decimais\r\n"
                      "- Deixe o espaço vazio!\n")

        if(permitido is True):

            acertou = chute == numero_secreto
            maior = chute > numero_secreto
            # menor = chute < numero_secreto

            if (acertou):
                mensagem_vitoria(pontuacao)
                break

            elif (maior):
                print("Seu chute foi alto,a resposta é menor!")
                round_atual += 1
                if(nivel_int == 1):
                    pontuacao -= pontos_a_perder
                elif(nivel_int == 2):
                    pontuacao -= pontos_a_perder
                elif(nivel_int == 3):
                    pontuacao -= pontos_a_perder

            else:  # if(menor):#se menor
                print("Seu chute foi baixo, a resposta é maior!")
                round_atual += 1
                if (nivel_int == 1):
                    pontuacao -= pontos_a_perder
                elif (nivel_int == 2):
                    pontuacao -= pontos_a_perder
                elif (nivel_int == 3):
                    pontuacao -= pontos_a_perder

        else:
            indice = tolerancia + 1
            break

    if(indice == tolerancia + 1):
        print("Paciência tem limites\n")
        print("       Fim do jogo")
        play_again()
    elif(round_atual == total_de_rounds + 1):
        mensagem_derrota(numero_secreto, pontuacao)
        play_again()
    else:
        print("       Fim do jogo!\n    Obrigado por Jogar!")
        play_again()


if(__name__ == "__main__"):
    jogar()
