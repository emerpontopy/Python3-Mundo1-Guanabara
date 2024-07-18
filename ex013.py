# DESAFIO 013 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salário = float(input("Qual é o salário do funcionário? R$ "))
aumento = float(input("Digite o aumento em %: "))
novo = salário + (salário * aumento / 100)
print("Um funcionário que ganhava R${:.2f}, com {}% de aumento, passa a receber R${:.2f}.".format(salário, aumento, novo))

