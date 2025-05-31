# Desafio 078 - Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e suas respectivas posições na lista.
lista = []
maior = menor = 0
for index in range(0,5):
    lista.append(int(input("Digite um valor: ")))
    if index == 0:
        maior = menor = lista[index]
    else:
        if lista[index] > maior: # Se index de lista[] for maior...
            maior = lista[index]
        if lista[index] < menor:
            menor = lista[index]
print(f"Já temos uma lista: {lista}")
print(f"O MAIOR número digitado foi {maior}, posição: ",end='')
for chave, valor in enumerate(lista):
    if valor == maior:
        print(f"{chave}...")

print(f"e o menor foi {menor}, na posição: ",end='')
for chave, valor in enumerate(lista):
    if valor == menor:
        print(f'{chave}...')
print("Cheguei ao final da lista.")

