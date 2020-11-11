"""
Desenvolva um algoritmo que leia um número inteiro X e um inteiro não-negativo N, calcule e escreva o valor de X^N (X elevado a N).

Entrada: Dois inteiros, X e N sendo N >= 0

Saida: Um número inteiro: resultado de X^N

Exemplos de Entrada e Saída
Entrada:
2 3
Saída:
8

Entrada:
-3 2
Saída:
9

Tinha uma pedra no meio do caminho

"""

a, b = list(map(int, input().split()))

print(a**b)
