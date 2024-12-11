# Desafio 061 - Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 PRIMEIROS TERMOS da progressão usando a estrutura WHILE.
print("Gerador de PA")
print("-="*10)
firstnum = int(input("Digite o primeiro termo: "))
constant = int(input("Qual é a razão da PA: "))
term = firstnum
count = 1
while count <= 10:
    print('{} -> '.format(term), end='')
    term += constant
    count += 1
print('FIM!')