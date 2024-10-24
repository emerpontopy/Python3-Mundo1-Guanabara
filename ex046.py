# DESAFIO 046 - Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
for cont in range(10,-1,-1):
    print(cont)
    sleep(1)
print('\033[31mPOW! KABUM! \033[0;0m')