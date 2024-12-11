# Desafio 062 - Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 TERMOS.
firstnum = int(input("Digite o primeiro termo: "))
constant = int(input("Digite a razão da PA: "))
count = 1
more = 10
repeat = 0
while more != 0:
    repeat = repeat + more
    while count <= repeat:
        print('{} -> '.format(firstnum), end='')
        firstnum += constant
        count += 1
    print('PAUSA')
    more = int(input("Quantos termos você quer mostrar a mais? "))
print("Progressão finalizada com {} termos mostrados. ".format(repeat))