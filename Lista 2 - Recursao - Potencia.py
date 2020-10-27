"""
Implemente uma função recursiva que, dados dois números inteiros x e n, calcula o valor de x^n.

Entrada
2
3

Saída
8
"""

base = int(input())
exp = int(input())

def pot(bas,potencia):
    if potencia == 1:
        return bas
    return bas * pot(bas, potencia-1)

print(pot(base, exp))