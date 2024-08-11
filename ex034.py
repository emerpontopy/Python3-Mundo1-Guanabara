# DESAFIO 034 - Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input("Digite o salário para saber quanto ficará após o aumento: R$"))
if sal <= 1250:
    print("O novo valor será de R$ {:.2f}.".format(sal + (sal * 0.15)))
else:
    print("O novo valor será de R$ {:.2f}.".format(sal + (sal * 0.10)))
# O meu programa ficou um pouco diferente do exemplo que Guanabara passou, criando uma variável para calcular a %, mas funciona da mesma forma :D