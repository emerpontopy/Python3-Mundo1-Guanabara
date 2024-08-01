# DESAFIO 031 - Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
from time import sleep
distance = float(input("Qual é a distância da sua viagem? "))
print("calculando a sua rota . . .")
sleep(2)
if distance <= 200:
    print("A sua passagem irá custar R${:.2f}.".format(distance * 0.50))
else:
    print("A sua passagem irá custar R${:.2f}.".format(distance * 0.45))
