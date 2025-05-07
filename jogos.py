import forca
import adivinhacao
def escolha_seu_jogo():
    print("*****************************************")
    print("***** Bem vindo a Seleção de jogos! *****")
    print('*****************************************\n')

    print("Escolha seu Jogo:", end="\n")
    i = 0

    while i != 1:
        print(" (1) Adivinhação \n (2) Forca (Manuntenção)! \n (3) Parar de Jogar.")
        jogo = input("Qual jogo você quer jogar?")

        if(jogo.isnumeric()):
            jogo = int(jogo)
            if(jogo == 1):
                print("\nJogar Advinhação!\n")
                adivinhacao.jogar()
                i = 1
                break
            elif(jogo == 2):
                print("\nEm Manuntenção!\n")
                # print("Jogar Forca!\n")
                # forca.jogar()
                # i = 1
                # break
            elif(jogo == 3):
                print("\nEncerrando Sistema...")
                i = 1
                break
            else:
                print("\nEste jogo não existe!\n")
                jogo = str(jogo)
        else:
            print("\nDigite apenas números!\n")

if(__name__ == "__main__"):
    escolha_seu_jogo()