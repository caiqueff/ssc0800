"""
Desenvolva um programa que leia quatro números inteiros e calcule a soma dos que forem par. Uma função chamada soma_par() deve receber esses quatro valores e retornar a soma dos pares.

Dica: use o seguinte print:

print("A soma dos numeros pares =", soma)
Exemplo de Entrada e Saída

Entrada:
2
0
4
3

Saída:
A soma dos numeros pares = 6
"""

val = list()
for i in range(1,5):
    val.append(input())
val = list(map(int, val))



def soma_par(val):
    soma = 0
    for i in val:
        if i%2 == 0:
            soma += i
    return soma

soma = soma_par(val)

print("A soma dos numeros pares =", soma)
