# Desafio 064 - Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a CONDIÇÃO DE PARADA. No final, mostre quantos números foram digitados e qual foi a soma entre entre eles (desconsiderando o flag "999").
num = count = soma = 0
num = int(input("Digite um número [999 para parar]: "))
while num != 999:
    soma += num
    count += 1
    num = int(input("Digite um número [999 para parar]: "))    
print("Você digitou {} números e a soma entre eles foi {}.".format(count, soma))