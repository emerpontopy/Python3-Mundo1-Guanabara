# Desafio 084 - Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista.
# No final, mostre: 
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
temp = list()
people = list()
lighter = heavier = 0
while True:
    temp.append(str(input("Nome: ")))
    temp.append(float(input("Peso: ")))
    if len(people) == 0:
        lighter = heavier = temp[1]
    else:
        if temp[1] > heavier:
            heavier = temp[1]
        if temp[1] < lighter:
            lighter = temp[1]
    people.append(temp[:])
    temp.clear()
    choose = str(input("Deseja continuar? [S/N] "))
    if choose in 'Nn':
        break
print(f"Foram cadastradas {len(people)} pessoas.")
print(f"O maior peso inserido foi {heavier}Kg. O peso de ", end='')
for p in people:
    if p[1] == heavier:
        print(f"[{p[0]}] ", end='')
print()
print(f"O menor peso foi de {lighter}Kg. O peso de ", end='')
for p in people:
    if p[1] == lighter:
        print(f"[{p[0]}] ", end='')
        