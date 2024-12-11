# Desafio 065 - Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a MÉDIA ENTRE TODOS os valores e qual foi o MAIOR e o MENOR valores lidos. O programa deve perguntar ao usuário se ele quer ou não CONTINUAR a digitar valores.

maior = menor = soma = count = 0
continuar = 'S'
while continuar in 'Ss':
    num = int(input("Digite um número: "))
    continuar = str(input("Quer continuar? [S/N] ")).upper().strip()
    soma += num
    count += 1
    media = soma / count
    if count == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
print("Você digitou {} números e a média foi de {}".format(count, media))
print("O maior valor foi {} e o menor foi {}".format(maior, menor))