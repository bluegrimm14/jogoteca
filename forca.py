import random
import jogos
import os

def mensagem_de_abertura():
    print("******************************************")
    print("******* Bem vindo ao Jogo de forca *******")
    print('******************************************\n')


def carrega_palavra_secreta(primeira_linha_valida=0):
    caminho_arquivo = os.path.join(os.path.dirname(__file__),"palavras.txt")
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        palavras = [linha.strip() for linha in arquivo]   

    """
    def carrega_palavra_secreta(primeira_linha_valida=0):
    caminho_arquivo = os.path.join(os.path.dirname(__file__), "palavras.txt")
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        palavras = [linha.strip() for linha in arquivo]
    """
    # for linha in arquivo:
    #     palavras.append(linha.strip())
    arquivo.close()

    numero = random.randrange(primeira_linha_valida, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def inicializa_letras(palavra):
    return ["_" for letra in palavra]


def regras_start(letras_acertadas, palavra_secreta, tentativas):
    print(letras_acertadas)
    print(f" - Regras\n"
          f"* Essa palavra tem {len(palavra_secreta)} letras.\n"
          f"* Você tem {tentativas} tentativas.\n"
          f"* Suas tentativas serão diminuidas a cada erro.\n"
          f"* Bom jogo! *")


def pede_chute():
    chute = input("Qual é a letra?:")
    chute = chute.strip().upper()
    return chute


def mensagem_vitoria(palavra_secreta):
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'        \n")
    print("Você ganhou!!! \n")
    print(f"palavra:{palavra_secreta.capitalize()}")
    print("\nObrigado por Jogar !")


def mensagem_derrota(palavra_secreta):
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
    print(f"Você perdeu. :(\nA palavra era {palavra_secreta.capitalize()}")
    print("Obrigado por Jogar !")


def desenha_forca(tentativas):
    print(r"  _______     ")
    print(r" |/      |    ")

    if (tentativas == 6):
        print(r" |      (_)   ")
        print(r" |            ")
        print(r" |            ")
        print(r" |            ")
    elif (tentativas == 5):
        print(r" |      (_)   ")
        print(r" |      \     ")
        print(r" |            ")
        print(r" |            ")
    elif (tentativas == 4):
        print(r" |      (_)   ")
        print(r" |      \|    ")
        print(r" |            ")
        print(r" |            ")
    elif (tentativas == 3):
        print(r" |      (_)   ")
        print(r" |      \|/   ")
        print(r" |            ")
        print(r" |            ")
    elif (tentativas == 2):
        print(r" |      (_)   ")
        print(r" |      \|/   ")
        print(r" |       |    ")
        print(r" |            ")
    elif (tentativas == 1):
        print(r" |      (_)   ")
        print(r" |      \|/   ")
        print(r" |       |    ")
        print(r" |      /     ")
    else:
        print(r" |      (_)   ")
        print(r" |      \|/   ")
        print(r" |       |    ")
        print(r" |      / \   ")
        print(r" |            ")
        print(r"_|___         ")
        print()


def confirma_chute_certo(palavra_secreta, chute, letras_acertadas, index):
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
            #  achou = True
        index += 1
    # tentativas -= 1
    print(letras_acertadas)


def play_again():
    escolhido = False
    while (escolhido is False):
        print("Você quer:\n"
              "* (1) Jogar denovo?\n"
              "* (2) Ir para seleção de Jogos?\n"
              "* (3) Parar de Jogar?\n")
        resposta = input("Selecione uma opção: ")
        if (resposta.isnumeric()):
            resposta = int(resposta)
            if (resposta == 1):
                print("Preparando Forca...\n")
                jogar()
                break
            elif (resposta == 2):
                print("Preparando Sala de Seleção...\n")
                jogos.escolha_seu_jogo()
                break
            elif (resposta == 3):
                print("Finalizando jogo...\n")
                break
        else:
            print("Escolha uma das opções, somente, e digite apenas números.")


def jogar():
    mensagem_de_abertura()

    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras(palavra_secreta)
    letras_chutadas = []

    enforcou = False
    acertou = False
    # tentativas = 4 + int(round(len(palavra_secreta) / 2))
    tentativas = 7

    regras_start(letras_acertadas, palavra_secreta, tentativas)

    while (not enforcou and not acertou):
        chute = pede_chute()
        if (chute.isalpha()):
            achou = False
            index = 0
            if (len(chute) == 1):
                if (chute not in letras_chutadas):
                    letras_chutadas.append(chute.upper())
                    if (chute in palavra_secreta):
                        confirma_chute_certo(palavra_secreta, chute, letras_acertadas, index)
                    elif (achou is False):
                        tentativas -= 1
                        desenha_forca(tentativas)
                        print(f"Esta palavra não contém a letra {chute}!")
                        print(letras_acertadas)
                    print(f"Faltam {tentativas} tentativas!")

                    print(f"As letras que você já chutou são:\n{letras_chutadas}")

                    enforcou = tentativas == 0
                    acertou = "_" not in letras_acertadas
                else:
                    print("Não chute letras repetidas!")
            else:
                print("Digite apenas uma letra!")
        else:
            print("Digite apenas letras!")

    if (acertou):
        mensagem_vitoria(palavra_secreta)
        play_again()
    else:
        mensagem_derrota(palavra_secreta)
        play_again()


if (__name__ == "__main__"):
    jogar()


