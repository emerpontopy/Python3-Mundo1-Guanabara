# DESAFIO 050 - Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma = 0
contador = 0
for c in range(1, 7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        soma += num
        contador += 1
print("Você digitou {} números pares e a soma deles é {}".format(contador, soma))