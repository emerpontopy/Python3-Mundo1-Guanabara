# DESAFIO 072 - Crie um programa que tenha uma TUPLA totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
num_tuple = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input("Digite um número entre 0 e 20: "))
    if 0 <= num <= 20:
        break
    else:
        print("Tente novamente. ",end='')
print(f'Você digitou o número {num_tuple[num].upper()}')