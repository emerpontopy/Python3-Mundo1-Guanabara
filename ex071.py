# Desafio 071 - Crie um programa que simule o funcionamento de um CAIXA ELETRÔNICO. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
saque = int(input("Qual o valor que você quer sacar? R$"))
total = saque
nota = 50 # maior nota de dinheiro
contanotas = 0 #contador do total de cada cédula
print(f"Para sacar a quantia de R${saque}")
while True:
    if total >= nota:
        total -= nota
        contanotas += 1
    else:
        if contanotas > 0:
            print(f"foram necessárias {contanotas} cédulas de R${nota}")
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        contanotas = 0
        if total == 0:
            break