# DESAFIO 012 - Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input("Digite o preço atual do produto: R$"))
desc = float(input("Digite o valor do desconto em % a ser aplicado: "))
final = preço - (preço * desc / 100)
print("O novo preço com {}% de desconto será de R${:.2f}.".format(desc, final))
