# DESAFIO 039 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade: - Se ele ainda vai se alistar ao serviço militar. - Se é a hora de se alistar. - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
nasc = int(input("Digite o ano em que você nasceu: "))
anoAtual = date.today().year
idade = anoAtual - nasc
if idade < 18:
    print("Você tem {} anos. Você ainda será convocado. Faltam {} anos para se alistar.".format(idade, (18-idade)))
elif idade == 18:
    print("É hora de se alistar! Procure a junta militar mais próxima.")
else:
    print("Você tem {} anos. Já passaram {} anos do tempo de se alistar. Procure uma junta militar IMEDIATAMENTE.".format(idade, (idade-18)))
