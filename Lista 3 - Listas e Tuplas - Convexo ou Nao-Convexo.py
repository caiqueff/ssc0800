"""
Dado um polígono simples (ou seja, um polígono cujos lados não adjacentes não se interceptam) P0P1P2...Pn-1 de n vértices, determinar se ele é côncavo ou convexo. Entrada: Um inteiro n>=3, indicando o número de vértices do polígono Em seguida, n linhas, contendo cada uma um par (x,y) de inteiros, representando o ponto P0,P1,P2,...,Pn-1 Obs: as arestas formadas são P0P1,P1P2,...,Pn-2Pn-1,Pn-1P0.

Saída: A string CONVEXO caso o polígono seja convexo, ou a string NAO CONVEXO, caso contrário.

Dica: se os pontos Pi=(x[i],y[i]), Pj=(x[j],y[j]), Pk=(x[k],y[k]) estão dispostos, nessa ordem, no sentido anti-horário, então o determinante da matriz ilustrada na imagem em arquivo abaixo será positivo. Se estiverem dispostos no sentido horário, será negativo. Tente desenhar alguns casos para ter uma ideia!

Exemplos de Entrada e Saída

Entrada:
5
0 0
1 0
2 3
-1 4
-3 1

Saída:
CONVEXO

Entrada:
7
1 2
5 3
4 5
3 4
2 6
0 3
2 3

Saída:
NAO CONVEXO
"""

def det(p1, p2, p3):
    prod = p1[0]*p2[1]+p2[0]*p3[1]+p3[0]*p1[1]
    prod -= p1[1]*p2[0] + p2[1]*p3[0] + p3[1]*p1[0]
    return prod

qnt = int(input())
pontos = []

for i in range(qnt):
    pontos.append(list(map(int, input().split())))

flag = 0
for i in range(len(pontos)):
    determinante = det(pontos[i%len(pontos)], pontos[(i+1)%len(pontos)], pontos[(i+2)%len(pontos)])
    if determinante != 0 and determinante * flag == 0:
        flag = determinante
    if flag*determinante < 0:
        print("NAO CONVEXO")
        break
else:
    print("CONVEXO")
