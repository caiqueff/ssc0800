"""
Dada uma sequência de números, encontre o número inteiro que aparece um número ímpar de vezes.

Nas soluções, sempre haverá apenas um número inteiro que aparece um número ímpar de vezes.

Exemplo:

Entrada:
1 1 1 1 3 2 2 4 4

Saída:
3
"""

nums = input().split()


def busca(lista):
    numero = lista.pop(0)
    if numero in lista:
        lista.pop(lista.index(numero))
        return busca(lista)
    else:
        return numero

print(busca(nums))