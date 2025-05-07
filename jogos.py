import forca
import adivinhacao
def escolha_seu_jogo():
    print("*****************************************")
    print("***** Bem vindo a Seleção de jogos! *****")
    print('*****************************************\n')

    print("Escolha seu Jogo:", end="\n")
    print(" (1) Adivinhação \n (2) Forca\n")
    i = 0

    while i != 1:
        jogo = input("Qual jogo você quer jogar?:")

        if(jogo.isnumeric()):
            jogo = int(jogo)
            if(jogo == 1):
                print("Jogar Advinhação!\n")
                adivinhacao.jogar()
                i = 1
                break
            elif(jogo == 2):
                print("Jogar Forca!\n")
                forca.jogar()
                i = 1
                break
            else:
                print("Este jogo não existe!\n")
                jogo = str(jogo)
        else:
            print("Digite apenas números!")

if(__name__ == "__main__"):
    escolha_seu_jogo()