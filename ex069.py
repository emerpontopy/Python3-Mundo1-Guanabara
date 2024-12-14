# Desafio 069 - Crie um programa que leia a IDADE e o SEXO de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o USUÁRIO quer ou não continuar. No final, mostre:
'''
A) Quantas pessoas têm mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres têm menos de 20 anos.
'''
adults = men = underageFem = 0
print('-'*13)
print('CADASTRE UMA PESSOA')
print('-'*13)
while True:
    age = int(input('Idade: '))
    sex = str(input('Sexo: [M/F] ')).strip().upper()
    choose = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while choose not in 'SsNn':
        choose = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if age > 18:
        adults += 1
    if sex == 'Mm' :
        men += 1
    if age < 20:
        underageFem += 1
    print('-'*13)
    
    if choose == 'N':
        break
    print('-'*13)
print('===== FIM DO PROGRAMA =====')
print(f'Total de pessoas com mais de 18 anos: {adults} \nAo todo temos {men} homens cadastrados \nE temos {underageFem} mulheres com menos de 20 anos')

