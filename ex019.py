# DESAFIO 019 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
al1 = str(input("Primeiro aluno: "))
al2 = str(input("Segundo aluno: "))
al3 = str(input("Terceiro aluno: "))
al4 = str(input("Quarto aluno: "))
lista = [al1, al2, al3, al4]
print("Quem vai apagar o quadro é: {}".format(choice(lista)))