"""
Dado um inteiro X calcule seu valor na Sequência de Fibonacci recursivamente

Entrada 1:
2
Saída 1:
1

Entrada 2:
6
Saída 2:
 8
"""

num = int(input())


def fibo(val):
    if (val == 1 or val == 2):
        return 1
    else:
        return fibo(val-1)+fibo(val-2)

print(fibo(num))