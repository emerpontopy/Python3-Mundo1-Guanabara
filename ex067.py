# Desafio 067 - Faça um programa que mostre a TABUADA de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será INTERROMPIDO quando o número solicitado for NEGATIVO. 
print('*'*18)
print('PROGRAMA TABUADA')
print('*'*18)
while True:
    num = int(input("Quer ver a tabuada de qual valor? "))
    if num < 0:
        break
    print('-'*33)
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    print('-'*30)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')