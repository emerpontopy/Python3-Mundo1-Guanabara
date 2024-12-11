# Desafio 060 - Faça um programa que leia um número qualquer e mostre o seu FATORIAL.
num = int(input("Digite um número positivo para saber o seu FATORIAL: "))
cont = num
fat = 1
print("Calculando {}! = ".format(num),end='')
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    fat *= cont
    cont -= 1
print('{}'.format(fat))
# from math import factorial
# num = int(input("Digite um número positivo para saber o seu FATORIAL: "))
# fat = factorial(num)
# print("O fatorial de {}! é {}.".format(num, fat))
'''acima em comentário é possível verificar
a solução mais simples, usando apenas
a biblioteca MATH'''