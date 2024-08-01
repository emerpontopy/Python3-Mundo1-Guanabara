#DESAFIO 025 - Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input("Qual é o seu nome completo? ")).strip()
print("Seu nome tem 'Silva'? {}".format('SILVA' in nome.upper()))
# aqui usamos o método 'strip' para eliminar possíveis espaços digitados erroneamente, como também o método 'upper' para garantir não deixar passar nada que possa ter sido escrito em minúsculo.