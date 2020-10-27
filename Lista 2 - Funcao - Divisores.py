"""
Crie uma função que use um número inteiro (n> 1) e retorne uma matriz com todos os divisores desse mesmo número (com exceção do 1 e do próprio número), do menor para o maior.

Caso o número seja primo, retorne a string '(inteiro) eh primo'.

Exemplo:

Entrada:
 3

Saída:
"eh primo"

Entrada:
 98

Saída:
[2, 7, 14, 49]
"""

n = int(input())

divisores = []

for i in range (2, n):
    if n%i == 0:
        divisores.append(i)

if(len(divisores) > 0):
    print(divisores)
else:
    print(f"{n} eh primo")
