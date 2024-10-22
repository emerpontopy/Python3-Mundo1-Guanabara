# DESAFIO 044 - Elabore um programaa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento: 
# - ÀVISTA DINHEIRO/CHEQUE: 10% de desconto
# - ÀVISTA NO CARTÃO: 5% de desconto
# - EM ATÉ 2X NO CARTÃO: PREÇO NORMAL
# - 3X OU MAIS NO CARTÃO: 20% DE JUROS
print("{:=^40}".format("Lojas EmerSongs"))
compras = float(input("Preço das compras: R$" ))
print('''FORMAS DE PAGAMENTO
[1] À VISTA DINHEIRO ou CHEQUE 
[2] À VISTA CARTÃO
[3] 2x no CARTÃO
[4] 3x ou mais no CARTÃO''')
formapgto = int(input("Qual é a forma de pagamento? "))
if formapgto == 1:
    total = compras - (compras * 10 / 100)    
elif formapgto == 2:
    total = compras - (compras * 5 / 100)    
elif formapgto == 3:
    total = compras
    vlParcela = total / 2
    print("Sua compra será parcelada em 2x de R${:.2f}".format(vlParcela))
elif formapgto == 4:
    total = compras + (compras * 20 / 100)
    parcelamento = int(input("Em quantas parcelas? "))
    vlParcela = total / parcelamento
    print("Sua compra será parcelada em {}x de R${:.2f} COM JUROS.".format(parcelamento, vlParcela))
else:
    total = compras
    print("\033[31mOPÇÃO INVÁLIDA de pagamento\033[0;0m. Tente novamente! ")
print("Sua compra de R${:.2f} vai custar R${:.2f} no final".format(compras, total))