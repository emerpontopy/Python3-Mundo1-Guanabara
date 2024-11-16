# DESAFIO 052 - Faça um programa que leia um número inteiro e diga se ele é ou não um NÚMERO PRIMO.
num = int(input("Digite um número: "))
divisible = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end='')
        divisible += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
if divisible == 2:
    print("\nO número \033[032m{} é um NÚMERO PRIMO!".format(num))
else:
    print("\n\033[0;0mO número \033[031m{} NÃO é um número primo.".format(num))