# DESAFIO 036 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. // Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
valorCasa = float(input("Digite o valor da casa: R$ "))
valorSalario = float(input("Digite o valor do salário: R$ "))
anos = int(input("Em quantos anos você quer pagar? "))
prestacao = valorCasa / (anos * 12)
minimo = valorSalario * 30 / 100
print("Para pagar uma casa no valor de R$ {:.2f} em até {} anos, parcela será de R$ {:.2f}.".format(valorCasa, anos, prestacao))
if prestacao <= minimo:
    print("O empréstimo pode ser CONCEDIDO!")
else:
    print("O empréstimo foi NEGADO!")
