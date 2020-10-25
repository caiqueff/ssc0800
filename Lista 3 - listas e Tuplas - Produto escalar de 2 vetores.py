"""
Dados dois vetores x e y, ambos com n elementos, determinar o produto escalar desses vetores. Exemplo: Produto escalar de x=(3,4) e y=(-2,5) é: x.y = 3.(-2) + 4.(5) = -6+20 = 14
A entrada terá 3 linhas: a primeira indicando o tamanho dos vetores, a segunda com os elementos do primeiro vetor e a terceira com os elementos do segundo vetor.

Nota: A saída deve apresentar duas casas decimais, como no exemplo abaixo.

Entrada: Um inteiro N Em seguida, 2 linhas, cada uma contendo as N coordenadas de cada vetor

Saída: O produto escalar entre esses vetores, formatado com 2 casas decimais

Exemplo de Entrada e Saída

Entrada:
4
1 2 4 5 
4 4 5 6

Saída:
62.00

Entrada:
4 
0.2 0.3 -5 -2.5
5 0.4 -2 -2

Saída:
16.12
"""

tamanho = int(input())

v1 = input().split()
v2 = input().split()

produto = 0
for i in range(tamanho):
    produto += float(v1[i])*float(v2[i])

print(f"{produto:.2f}")