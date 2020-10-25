"""
Dados 3 pontos no plano, decida se eles formam um triângulo ou não; em caso positivo, determinar se ele é acutângulo (todos seus ângulos internos medem menos que 90º), retângulo (possui um ângulo interno reto) ou obtusângulo (possui um ângulo interno de medida maior que 90º). Considere o exercício do produto escalar entre 2 vetores como dica, pense quando ele é positivo, zero ou negativo!

https://www.geeksforgeeks.org/find-all-angles-of-a-triangle-in-3d/

Entrada: 3 linhas, cada uma contendo um par de inteiros indicando as coordenadas (x,y) de cada ponto.

Saída: A string NAO, caso os pontos não formem um triângulo. Caso formem, imprima a string SIM, e na linha de baixo: A, caso seja acutângulo, R caso seja retângulo ou O caso seja obtusângulo.

Exemplos de Entrada e Saída

Entrada
0 4
0 0
3 0

saída
SIM
R

Entrada
5 4
3 2
6 1

saída
SIM
A

Entrada
0 0
-1 -1
1 1

saída
NAO
"""

p1 = list(map(int, input().split())) 
p2 = list(map(int, input().split())) 
p3 = list(map(int, input().split())) 

def cos(a, b, c):

    x1, y1 = a[0], a[1]
    x2, y2 = b[0], b[1]
    x3, y3 = c[0], c[1]
  
    num = (x2-x1)*(x3-x1)+(y2-y1)*(y3-y1)
    den = pow(((x2-x1)**2+(y2-y1)**2)*((x3-x1)**2+(y3-y1)**2), 1/2)
  
    cos = num / den
  
    return cos
  
A = cos(p1, p2, p3)
B = cos(p2, p3, p1)
C = cos(p3, p1, p2)

if (A**2==1 or B**2==1 or C**2 == 1):
    print("NAO")
elif (A==0 or B==0 or C==0):
    print("SIM")
    print("R")
elif (A<0 or B<0 or C<0):
    print("SIM")
    print("O")
else:
    print("SIM")
    print("A")