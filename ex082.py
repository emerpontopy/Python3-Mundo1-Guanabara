# Desafio 082 - Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie DUAS LISTAS EXTRAS que vão conter apenas os valores PARES e 
# os valores ÍMPARES digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.
numlist = []
even = []
odds = []
while True:
    numlist.append(int(input("Digite um número: ")))
    choose = str(input("Deseja continuar? [S/N] "))
    if choose in 'Nn':
        break

print("-="*30) 
for i, v in enumerate(numlist):
    if v % 2 == 0:
        even.append(v)
    elif v % 2 == 1:
        odds.append(v)
print(f"Todos os números digitados foram {numlist}.")
print(f"Os números pares foram {even}.")
print(f'Os números ímpares foram {odds}.')