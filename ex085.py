# Desafio 085 - Crie um programa onde o usuário possa digitar SETE valores númericos 
# e cadastre-os em uma LISTA ÚNICA que mantenha separados os valores PARES e ÍMPARES.
# No final, mostre os valores pares e ímpares em ordem crescente.
numlist = [[], []]
valor = 0
for c in range(1,8):
    valor = int(input(f"Digite o {c}º valor: "))
    if valor % 2 == 0:
        numlist[0].append(valor)
    else:
        numlist[1].append(valor)
print("-="*30)
numlist[0].sort()
numlist[1].sort()
print(f"Os valores pares digitados foram: {numlist[0]}")
print(f"Os valores ímpares digitados foram: {numlist[1]}")
