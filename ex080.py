# # Desafio 080 - Crie um programa onde o usuário possa digitar CINCO valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela. 
numlist = []
for c in range(0,5):
    num = int(input("Digite um valor: "))
    if c == 0 or num > numlist[-1]: # '[-1]' é assim que eu chamo o último elemento
        numlist.append(num)
        print('Adicionado no final da lista . . .')
    else:
        pos = 0 # variável contadora
        while pos < len(numlist):
            if num <= numlist[pos]:
                numlist.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista. . .')
                break
            pos += 1
print('-=-'*30)
print(f'Os valores adicionados em ordem foram: {numlist}')
# 'Sem o sort()', ou seja, utilizando laços de repetição aninhados com variáveis condicionais
# para contar cada um dos itens da lista e colocar-los na posição correta.