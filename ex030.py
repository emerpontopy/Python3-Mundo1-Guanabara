# DESAFIO 030 - Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input("Diga-me um número qualquer: "))
resultado = num % 2
if resultado == 0:
    print("O número digitado é PAR.")
else:
    print("Esse número é ÍMPAR.")

# Lembre-se: o resto da divisão de qualquer número PAR é 0, o resto da divisão de qualquer número ÍMPAR é 1.