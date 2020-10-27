"""
Dados dois números inteiros X e Y

Calcule MDC(X,Y) recursivamente

Entrada
12
9

Saida
3
"""

num1 = int(input())
num2 = int(input())


def mdc(x,y):
    if y>x:
        x,y = y,x
    if(x%y == 0):
        return y
    else:
        return mdc(y,x%y)

print(mdc(num1,num2))