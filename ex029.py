# DESAFIO 029 - Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite. 
velocidade_registrada = float(input("Qual é a velocidade atual do carro? "))
velocidade_permitida = 80
multa = (velocidade_registrada - velocidade_permitida) * 7
if velocidade_registrada > velocidade_permitida:
    print("MULTADO! Você excedeu o limite permitido que é de 80Km/h. Você deve pagar uma multa de R${:.2f}!".format(multa))
else:
    print("Tenha um bom dia! Dirija com segurança.")
