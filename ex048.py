# DESAFIO 048 - Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
multiplos = 0 # isso é um contador
soma = 0
for num in range(1,501, 2):
    if num % 3 == 0:
        multiplos += 1
        soma += num
print("A soma de todos os {} valores solicitados é {}".format(multiplos, soma))