# DESAFIO 035 - Desenvolva um programa que leia o comprimento de três segmentos de reta e diga ao usuário se elas podem ou não formar um triângulo.

# BRASIL ESCOLA: Para que os três segmentos formem um triângulo, existe o que conhecemos como condição de existência, que é a seguinte: a soma de dois lados é sempre menor que o terceiro lado.
r1 = int(input("Primeiro lado: "))
r2 = int(input("Segundo lado: "))
r3 = int(input("Terceiro lado: "))
if r1 + r2 < r3 and r2 + r3 < r1 and r3 + r1 < r2:
    print("Esses segmentos formam um triângulo!")
else:
    print("Não forma um triângulo.")
