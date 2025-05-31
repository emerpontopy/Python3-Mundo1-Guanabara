# Desafio 081 - Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso mostre:
# A) Quantos números foram digitados.
# B) A lista de valores ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista. 
numlist = []
while True:
    num = int(input("Digite um número: "))
    numlist.append(num)
    choose = str(input("Vai digitar mais algum número? Sim [S] | Não [N] "))
    if choose in 'Nn':
        break
numlist.sort(reverse=True)
print("-="*30)
print(f"Foram digitados {len(numlist)} números.")
print(f"A lista digitada em ordem decrescente foi {numlist}")
if 5 in numlist:
    print("O número 5 foi digitado.")
else:
    print("O número 5 NÃO foi digitado.")
print("-="*30)
