# Desafio 079 - Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele NÃO SERÁ ADICIONADO. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
numlist = []
while True:
    num = int(input("Digite um valor: "))
    if num not in numlist:
        numlist.append(num)
        print("Valor digitado com sucesso!")
    else:
        print("Valor DUPLICADO. Não pode ser adicionado...")
    choose = input(str("Deseja continuar? [S/N] "))
    if choose in 'Nn':
        break
numlist.sort()
print('-='*30)
print(f'Os valores adicionados foram {numlist}')