# Desafio 070 - Crie um programa que leia o NOME e o PREÇO de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
'''
A) Qual é o TOTAL GASTO na compra. 
B) Quantos produtos custam mais de R$1000
C) Qual é o nome do produto mais barato'''
print('-'*50)
print('{:^50}'.format('SUPER EMMERCADO'))
print('-'*50)
maismil = total = index = menor = 0
barato = ''
while True:
    prod = str(input('Nome do produto: '))
    price = float(input('Preço R$: '))
    total += price
    index += 1
    if price > 1000:
        maismil += 1
    if index == 1 or price < menor: # nome do menor produto e seu valor
        menor = price
        barato = prod
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:10.2f}')
print(f'Temos {maismil} produtos custando mais de R$1000')
print(f'O produto mais barato foi o item nº {index}, {barato}, que custa R${menor:.2f}')