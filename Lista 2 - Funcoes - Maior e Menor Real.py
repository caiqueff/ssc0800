"""
Desenvolva um programa que receba 10 valores reais e utilize duas funções para retornar, respectivamente, o menor e o maior deles. O uso de funções é obrigatório. Em seguida, escreva o resultado com precisão de 2 casas decimais conforme exemplo.

Entrada: 10 números reais

Saida: Duas linhas, com o menor e o maior valor dentre os 10 valores digitados respectivamente. Utilize 2 casas decimais.

Exemplos de Entrada e Saída

Entrada:
1
10
14
4
95.4
8
15
43
17
3

Saída:
1.00
95.40

Entrada:
43.45
-1.22
-10.21
25.93
-25.85
48.14
80.22
18.98
10.63
46.92

Saída:
-25.85
80.22
"""

numeros = []
for i in range(0,10):
    numeros.append(input())

numeros = list(map(float, numeros))
numeros.sort()

def maior(nums):
    maior = nums[0]
    for i in nums:
        if i>maior:
            maior = i
    return maior

def menor(nums):
    menor = nums[0]
    for i in nums:
        if i<menor:
            menor = i
    return menor

print(f"{menor(numeros):.2f}")
print(f"{maior(numeros):.2f}")
