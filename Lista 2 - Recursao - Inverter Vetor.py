"""
Dado um VETOR de inteiros, inverta a posição dos seus elementos RECURSIVAMENTE.

Entrada
0 1 2 3 4 5 6 7 8 9
Saida
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
"""

nums = list(map(int, input().split()))


def busca(lista, n):
    if n == 1:
        return lista
    lista.insert(n-1, lista.pop(0))
    return busca(lista, n-1)

print(busca(nums, len(nums)))