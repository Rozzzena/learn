from random import randint
computador = randint(0,2)

def JOKENPO(PC, Player):
    if PC == 0:            #PC JOGA PEDRA
        if Player == 0:
            print("EMPATE")

        elif Player == 1:
            print("VITÓRIA")

        elif Player == 2:
            print("DERROTA")

    elif PC == 1:           #PC JOGA PAPEL
        if Player == 0:
            print("DERROTA")

        elif Player == 1:
            print("EMPATE")

        elif Player == 2:
            print("VITÓRIA")

    elif PC == 2:           #PC JOGA TESOURA
        if Player == 0:
            print("VITÓRIA")

        elif Player == 1:
            print("DERROTA")

        elif Player == 2:
            print("EMPATE")

print(''' Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA ''')

jogador = int(input("Insira: "))

itens = ("Pedra", "Papel", "Tesoura")

print('-=' * 20)
print("Computador jogou {}".format(itens[computador]))
print("Jogador jogou {}".format(itens[jogador]))
print('-=' * 20)


JOKENPO(computador, jogador)