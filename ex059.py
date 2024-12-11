# Desafio 059 - Crie um programa que leia dois valores e mostre um menu na tela:
'''
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
'''
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
end = False
while not end:
    choose = int(input('''
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
>>> Qual é a sua opção?
'''))
    if choose == 1:
        result = num1 + num2
        print("A soma entre {} + {} é {}".format(num1, num2, result))
        print('=-='*13)
    elif choose == 2:
        result = num1 * num2
        print("A multiplicação de {} x {} é {}".format(num1, num2, result))
        print('=-='*13)
    elif choose == 3:
        if num1 > num2:
            result = num1
            print("O MAIOR número entre {} e {} é {}.".format(num1, num2, result))
            print('=-='*13)
        elif num1 < num2:
            result = num2
            print("O MAIOR número entre {} e {} é {}.".format(num1, num2, result))
            print('=-='*13)
        else:
            print("Os números são iguais!")
            print('=-='*13)
    elif choose == 4:
        print("OK. Vamos analisar novos números!")
        num1 = int(input("Digite o primeiro valor: "))
        num2 = int(input("Digite o segundo valor: "))
    elif choose == 5:
        print("Finalizando . . . ")
        sleep(2)
        break
    else:
        print("OPÇÃO INVÁLIDA. Digite uma das opções disponíveis:")
print('=-='*13)
print("Fim do programa. Até a próxima!")