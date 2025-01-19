# DESAFIO 075 - Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3. 
# C) Quais foram os números pares.
num_tuple = (int(input("Digite um número: ")), int(input("Digite outro número: ")), int(input("Digite mais um número: ")), int(input("Digite o último número: ")))
print(f'Você digitou os valores {num_tuple}')
print(f'O valor 9 apareceu {num_tuple.count(9)} vezes.')
print(f'O valor 3 foi digitado na {num_tuple.index(3)+1}ª posição.')
print(f'Os números pares foram: ')
for c in num_tuple:
    if c % 2 == 0:
        print(c,end=' ')