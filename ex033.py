# DESAFIO 033 - Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
# verificando qual é o menor número digitado
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print("O menor número é {}".format(menor))

# verificando qual é o MAIOR número digitado
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("e o maior número é {}".format(maior))
