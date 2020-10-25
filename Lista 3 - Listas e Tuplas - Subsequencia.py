"""
Uma sequência pode ser interpretada como uma lista finita de termos. Faça um programa que leia um numero N; em seguida, na linha debaixo, leia todos os elementos de uma sequência de inteiros, armazene-os numa lista e verifique se existe uma subsequência tal que a soma dos termos é N, imprimindo "SIM" em caso positivo e "NAO" em caso negativo. Obs: uma subsequência é formada pegando uma parte da sequência original, sem pular nenhum termo; por exemplo, se (2,3,4,11,6,7,8) é a nossa sequência, (4,11,6) e (2) são subsequências dela, enquanto que (3,11,6,7) não é.

Entrada: Um inteiro N

Saída: A string SIM, caso haja uma subsequência cuja soma dos termos seja N; caso contrário, imprima a string NAO.

Exemplos de Entrada e Saída

Entrada:
12
1 2 3 4 5

Saída:
SIM
(A subsequência (3,4,5) tem soma dos termos igual a 12)

Entrada:
12
8 3 4

Saída:
NAO
"""

valor = int(input())
numeros = list(map(int, input().split()))

#For que define quantos numeros tera a sequencia (de 1 até o maximo)
for i in range(1, len(numeros)):
    #For que define onde inicia a sequencia de i numeros
    for j in range(len(numeros)-i+1):
        sum = 0
        #For que soma todos os i numeros começando pelo índice j
        for k in range(j,j+i):
            sum+=numeros[k]
        if sum == valor:
            print("SIM")
            break
    else:
        continue
    break
else:
    print("NAO")
