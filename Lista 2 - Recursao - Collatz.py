"""
A conjetura de Collatz foi elaborada pelo alemão matemático Lothar Collatz, tendo sido proposta no ano de 1937. Nela, aplica-se a qualquer número natural e nos diz que, se o número for par, para dividi-lo por 2, e se for ímpar, para o multiplicar por 3 e somar 1.

Considere a seguinte operação em um número inteiro positivo arbitrário:

Se o número é par, divida-o por 2;
Se for ímpar, multiplique-o por 3 e some 1
Sua missão é criar uma função, usando recursividade, que aplique a conjectura de Collatz. A função deve receber um número inteiro positivo n e mostrar sua sequência até que resulte o número 1.

Exemplo:

Entrada:
234

Saída:
234 117 352 176 88 44 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
"""

num = int(input())

numeros = []
def collatz(num):
    print(int(num), end=" ")
    if num == 1:
        return 1
    if num%2 == 0:
        return collatz(num/2)
    else:
        return collatz(num*3 +1)

collatz(num)
