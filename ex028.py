# DESAFIO 028 - Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
num = random.randint(1, 5)
palpite = int(input("Estou pensando em um número entre 1 e 5. Digite e tente adivinhar qual número é: "))
if num == palpite:
    print("Acertou! Você venceu.")
else:
    print("Errou! Você perdeu.")
print("O número que eu escolhi foi o {}".format(num))
