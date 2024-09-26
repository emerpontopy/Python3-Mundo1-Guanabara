# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo: Abaixo de 18.5 (Abaixo do Peso); Entre 18.5 e 25 (Peso ideal); 25 até 30 (Sobrepeso); 30 até 40 (Obesidade); Acima de 40 (Obesidade mórbida)
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: "))
IMC = peso / (altura * altura)
print("Seu IMC é de {:.1f}".format(IMC))
if IMC < 18.5:
    print("Você está \033[1;31m ABAIXO DO PESO \033[0;0m")
elif IMC >= 18.5 and IMC < 25:
    print("Você tem o \033[1;94m PESO IDEAL \033[0;0m")
elif IMC >= 25 and IMC < 30:
    print("Você tem um \033[1;95m SOBREPESO \033[0;0m")
elif IMC >= 30 and IMC < 40:
    print("Você está em\033[1;35m OBESIDADE \033[0;0m")
elif IMC > 40:
    print("Você tem\033[1;31m OBESIDADE MÓRBIDA \033[0;0m")