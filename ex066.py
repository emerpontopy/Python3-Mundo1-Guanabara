# Desafio 066 - Crie um programa que leia VÁRIOS NÚMEROS inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a CONDIÇÃO DE PARADA. No final, mostre QUANTOS NÚMEROS foram digitados e qual foi a soma entre eles (desconsiderando a flag).
num = sum = count = 0
while True:
    num = int(input("Digite um número [999 para parar]: "))
    if num == 999:
        break
    sum += num 
    count += 1 # foi importante colocar essa iteração após o break para desconsiderar o '999'
print(f"Um total de {count} números foram digitados e a soma entre eles é igual a {sum}.")