"""
Faça um programa que leia uma sequência de números terminada em -1 e imprima a soma dos números pares lidos. Dica: Utilize a função implementada no exercício Soma Pares Parte I.

Entrada: Sequência de números com tamanho desconhecido terminada em -1

Saida: A soma dos números pares lidos

Exemplos de Entrada e Saída
Entrada:
7 5 2 2 6 9 8 7 -1

Saída:
18

Entrada:
-1

Saída:
0
"""

val = input().split()
val = list(map(int, val))

def soma_par(val):
    soma = 0
    for i in val:
        if i%2 == 0:
            soma += i
    return soma

soma = soma_par(val)

print(soma)
