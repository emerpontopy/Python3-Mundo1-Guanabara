# Desafio 087 - Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados. 
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
evenSum = trdColumnSum = scnRowLargest = 0
for row in range(0, 3):
    for column in range(0, 3):
        matrix[row][column] = int(input(f'Digite um valor para [{row}, {column}]: '))
        if matrix[row][column] % 2 == 0:
            evenSum += matrix[row][column]
print("-="*30)
for row in range(0, 3):
    for column in range(0, 3):
        print(f"[{matrix[row][column]:^5}]", end='')
    print()
print("-="*30)
print(f'A soma dos valores pares é {evenSum}.')
for row in range(0, 3):
    trdColumnSum += matrix[row][2]
print(f'A soma dos valores da terceira coluna é {trdColumnSum}.')
for column in range(0, 3):
    if column == 0:
        scnRowLargest = matrix[1][column]
    elif matrix[1][column] > scnRowLargest:
        scnRowLargest = matrix[1][column]
print(f'O maior valor da segunda linha é {scnRowLargest}.')