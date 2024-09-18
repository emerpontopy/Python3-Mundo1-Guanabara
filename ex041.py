# DESAFIO 040 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade: - Até 9 anos: MIRIM; Até 14 anos: INFANTIL; Até 19 anos: JUNIOR; Até 20 anos: SÊNIOR; Acima: MASTER
from datetime import date
AnoAtual = date.today().year
AnoNasc = int(input("Digite o seu ano de nascimento e descubra sua categoria: "))
idade = AnoAtual - AnoNasc
if idade <= 9:
    print("Você faz parte da categoria MIRIM.")
elif idade <= 14:
    print("Você faz parte da categoria INFANTIL.")
elif idade <= 19:
    print("Você faz parte da categoria JUNIOR.")
elif idade <= 25:
    print("Você faz parte da categoria SÊNIOR.")
else:
    print("Você faz parte da categoria MASTER.")
