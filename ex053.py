# DESAFIO 053 - Crie um programa que leia uma frase qualquer e diga se ela é um PALÍNDROMO, desconsiderando os espaços. 
frase = str(input("Digite uma frase: ")).strip().upper() #elimina espaços anteriores e posteriores e deixa tudo em maiúsculo
palavras = frase.split() # elimina os espaços internos
junto = ''.join(palavras) # juntar tudo numa varíavel
inverso = ''
# inverso = junto[::-1] << dá pra fazer sem o laço FOR, apenas por fatiamento da string
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra] # contando da última letra até a primeira
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("A frase digitada NÃO é um palíndromo!")

