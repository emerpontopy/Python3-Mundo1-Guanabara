# DESAFIO 045 - Crie um programa que faça o computador jogar Jokenpô com você.
import random
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0,3) #precisei editar aqui pois não estava seguindo o 'stop+1' do método
print('''Escolha sua opção:
      [ 0 ] PEDRA
      [ 1 ] PAPEL
      [ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
if jogador != 0 and jogador != 1 and jogador !=2:
    print("\033[31mOPÇÃO INVÁLIDA. \n Tente novamente!\033[0;0m")
    quit()
else:
    print("\033[1;35mJO\033[0;0m")
    sleep(1)
    print("\033[1;36mKEN\033[0;0m")
    sleep(1)
    print("\033[1;33mPO!!!\033[0;0m")
    print("-=-"*10)
    print("\033[1;47mO Computador jogou {}".format(itens[computador]))
    print("O Jogador jogou {}\033[0;0m".format(itens[jogador]))
    print("-=-"*10)
    if computador == 0: # computador jogou PEDRA
        if jogador == 0:
            print("EMPATE")
        elif jogador == 1:
            print("JOGADOR VENCEU")
        elif jogador == 2:
            print("COMPUTADOR VENCEU")
        else:
            print("\033[31mOPÇÃO INVÁLIDA. Tente novamente!\033[0;0m")
    elif computador == 1: # computador jogou PAPEL
        if jogador == 0:
            print("COMPUTADOR VENCEU")
        elif jogador == 1:
            print("EMPATE")
        elif jogador == 2:
            print("JOGADOR VENCEU")
        else:
            print("\033[31mOPÇÃO INVÁLIDA. Tente novamente!\033[0;0m")
    elif computador == 2: # computador jogou TESOURA
        if jogador == 0:
            print("JOGADOR VENCEU")
        elif jogador == 1:
            print("COMPUTADOR VENCEU")
        elif jogador == 2:
            print("EMPATE")
        else:
            print("\033[31mOPÇÃO INVÁLIDA. Tente novamente!\033[0;0m")