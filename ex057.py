# Desafio 057 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
profileSex = str(input("Digite o sexo da pessoa \n[M] Masculino \n[F] Feminino\n: ")).strip().upper()[0]
while profileSex not in 'MmFf':
    profileSex = str(input("Dados incorretos. Digite uma opção válida: [M] ou [F] ")).strip().upper()[0]
print("Sexo '{}' digitado corretamente.".format(profileSex))