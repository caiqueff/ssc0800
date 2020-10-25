"""
Desenvolva um algoritmo que leia um conjunto de 20 valores inteiros, guarde-os em uma lista e troque a sua ordem. Ou seja, o programa deve trocar lista[0] com lista[19], lista[1] com lista[18] e assim por diante.

Entrada: Uma linha com 20 números inteiros.

Saida: Os mesmos 20 números em ordem inversa, um por linha.

Exemplos de Entrada e Saída

Entrada:
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

Saída:
20
19
18
17
16
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
"""

numeros = input().split()

for i in range(len(numeros),0,-1):
    print(numeros[i-1])
