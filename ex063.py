# Desafio 063 - Escreva um programa que leia um número n inteiro e mostre na tela os n primeiros elementos de uma SEQUÊNCIA DE FIBONACCI.
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input("Quantos termos você quer mostrar? "))
a = 5
b = 6
print('{} -> {}'.format(a, b), end='')
count = 3
while count <= n:
    c = a + b
    print(' -> {}'.format(c), end='')
    a = b
    b = c
    count += 1
print(' -> FIM')