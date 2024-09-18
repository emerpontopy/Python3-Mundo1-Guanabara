# DESAFIO 042 - Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: - EQUILÁTERO (todos os lados iguais) - ISÓSCELES (dois lados iguais) - ESCALENO (todos os lados diferentes)
r1 = float(input("Primeiro lado: "))
r2 = float(input("Segundo lado: "))
r3 = float(input("Terceiro lado: "))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print("Esses segmentos formam um triângulo ", end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print("Esses segmentos NÃO formam um triângulo.")