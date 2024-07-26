# DESAFIO 020- O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
al1 = str(input("Primeiro nome: "))
al2 = str(input("Segundo nome: "))
al3 = str(input("Terceiro nome: "))
al4 = str(input("Quarto nome: "))
alunos = [al1, al2, al3, al4]
# obtive o resultado NONE ao passar: print("A ordem sorteada será {}".format(shuffle(alunos)))
# preciso fazer o embaralhamento da lista antes de chama-la
shuffle(alunos)
# também não foi possível usar a string formatada, então chamei duas linhas do comando 'print'
print("A ordem de aprensentação será: ")
print(alunos)
