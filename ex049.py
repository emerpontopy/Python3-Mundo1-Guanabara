# DESAFIO 049 - Refaça o Desafio 009, mostrando a tabuada de um número que o usuário escolher, só qeu agora utilizando um laço FOR
num = int(input("Digite um número inteiro e descubra sua tabuada: "))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))
