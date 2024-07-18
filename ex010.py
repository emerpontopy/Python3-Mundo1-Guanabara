# DESAFIO 010 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. cotação USD em 13/JUL/2024
real = float(input("Quanto dinheiro você tem na carteira? R$"))
dolar = real / 5.42
print("Com R${:.2f} você pode comprar US${:.2f}".format(real, dolar))
