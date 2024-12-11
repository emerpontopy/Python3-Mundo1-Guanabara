# Desafio 058 - Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um NÚMERO ENTRE 0 E 10. Só que agora o jogador vai tentar até acertar, mostrando no final quantos palpites foram necessários para vencer. 
# acho que vale criar um acumulador para imprimir o resultado no final
from random import randint
num = randint(1,10)
print("Olá, jogador! Estou pensando em um número entre 0 e 10. \nSerá que você consegue adivinhar qual é? ")
bet = int(input("Qual é o seu palpite? "))
attempt = 1 # acumulador
while bet != num:
    if bet < num:
        bet = int(input("Mais... Tente mais uma vez. \nQual é seu palpite? " ))
        attempt += 1
    elif bet > num:
        bet = int(input("Menos... Tente mais uma vez. \nQual é seu palpite? "))
        attempt += 1
if bet == num:
    print("Acertou com {} tentativas. Parabéns!".format(attempt))