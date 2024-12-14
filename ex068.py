# Desafio 068 - Faça um programa que jogue PAR OU ÍMPAR com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no jogo. 
from random import randint
victory = 0
print('=-'*13)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*13)
while True:
    numjog = int(input("Digite um valor: "))
    pcjog = randint(1,11)
    sum = numjog + pcjog
    type = str(input("Você quer Par ou Ímpar? [P/I] ")).strip().upper()[0]
    while type not in 'PI':
        type = str(input("Você quer Par ou Ímpar? [P/I] ")).strip().upper()[0]
    print('-'*50)
    print(f"Você jogou {numjog} e o computador {pcjog}. Total de {sum},",end='')
    print(' DEU PAR.' if sum % 2 == 0 else ' DEU ÍMPAR.')
    print('-'*50)
    if type == 'P':
        if sum % 2 == 0:
            print("Você VENCEU! \nVamos jogar novamente...")
            victory += 1
        else:
            print("Você PERDEU!")
            break
    elif type == 'I':
        if sum % 2 == 1:
            print(f"Você VENCEU! \nVamos jogar novamente...")
            victory += 1
        else:
            print("Você PERDEU!")
            break
print(f"Você conseguiu um total de {victory} vitórias consecutivas! ")