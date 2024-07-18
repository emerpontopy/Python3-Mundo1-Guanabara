# DESAFIO 008 - Escreva um programa que leia um valor em metros e o exiba em centímetros e mílimetros.
medida = float(input("Escreva uma distância em metros: "))
cm = medida * 100
mm = medida * 1000
print("A medida de {}m corresponde a {:.0f}cm e em milímetros é {:.0f}mm.".format(medida, cm, mm))

