"""
Desenvolva uma função recursiva que consiga calcular o fatorial de um determinado numero inteiro positivo (n>0).

Entrada:
 10

Saída:
 3628800
"""

numero = int(input())

def fatorial(num):
    if num == 1:
        return num
    return num*fatorial(num-1)

print(fatorial(numero))