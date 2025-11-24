# Desafio 086 - Crie um programa que crie uma MATRIZ de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a MATRIZ na tela, com a formatação correta.
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for row in range(0, 3):
    for column in range(0, 3):
        matriz[row][column] = int(input(f'Digite um valor para [{row}, {column}]: '))
print("-="*30)
for row in range(0, 3):
    for column in range(0, 3):
        print(f"[{matriz[row][column]:^5}]", end='')
    print()
    