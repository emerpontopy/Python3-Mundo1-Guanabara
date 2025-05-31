# Desafio 083 - Crie um programa onde o usuário digite uma EXPRESSÃO NÚMERICA qualquer
# que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os
# parênteses abertos e fechados na ordem correta.
expr = str(input('Digite a expressão numérica: '))
pilha = []
for simbol in expr:
    if simbol == '(':
        pilha.append('(')
    elif simbol == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print("Sua expressão é válida!")
else:
    print("Ops, sua expressão é inválida.")
