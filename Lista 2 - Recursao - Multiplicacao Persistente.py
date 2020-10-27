"""
Escreva uma função que aceite um inteiro (n>0) e calcule os produtos dos seus digitos até que um único digito seja alcançado. A função deve retornar esse ultimo digito.

Exemplo:

39  // 3*9 = 27, 2*7 = 14, 1*4 = 4

Entrada:
39
Saída
4
"""
num = input()


def calcula(val):
    if(len(val) == 1):
        return val
    else:
        soma = 1
        for i in range(len(val)):
            soma *= int(val[i])
        #print(soma)
        return calcula(str(soma))

print(calcula(num))