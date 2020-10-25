"""
Dados N (N>=3) pontos no plano, determinar se existe algum subconjunto de 3 elementos que determina uma circunferência de raio R. Dica: pense na equação de uma circunferência!

http://ambrsoft.com/trigocalc/circle3d.htm

https://mundoeducacao.bol.uol.com.br/matematica/determinando-centro-uma-circunferencia.htm

https://www.ime.unicamp.br/~deleo/MA141/a33.pdf

Entrada: Na primeira linha, dois inteiros: N e R, indicando o número de pontos e o raio da circunferência; em seguida, N linhas, cada uma contendo um par (x,y) de inteiros indicando os pontos no plano xy. Saída: O caractere S, caso exista um trio de pontos que determina uma circunferência, ou o caractere N, caso contrário.

Exemplos de Entrada e Saída

Entrada
4 2
2 0
0 2
1 1
0 -2

Saída
S
(Nesse caso, os pontos (2,0), (0,2) e (0,-2) determinam uma circunferência de raio 2)

Entrada
4 7
1 1
-1 2
0 0
0 -3

Saída
N
"""

n, raio = list(map(int, input().split()))

p = []

for i in range (0,n):
    p.append(list(map(int, input().split())))

enc = False

for i in range(0, n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            x1, y1 = p[i][0], p[i][1]
            x2, y2 = p[j][0], p[j][1]
            x3, y3 = p[k][0], p[k][1]
            a = x1*y2 + x3*y1 + x2*y3 - x3*y2 - x1*y3 - x2*y1
            b = -(((x1**2)+(y1**2))*y2 + ((x2**2)+(y2**2))*y3 + ((x3**2)+(y3**2))*y1 - ((x3**2)+(y3**2))*y2 - ((x1**2)+(y1**2))*y3 - ((x2**2)+(y2**2))*y1)
            c = ((x1**2)+(y1**2))*x2 + ((x3**2)+(y3**2))*x1 + ((x2**2)+(y2**2))*x3 - ((x3**2)+(y3**2))*x2 - ((x1**2)+(y1**2))*x3 - ((x2**2)+(y2**2))*x1
            if a != 0:
                xc = -b/(2*a)
                yc = -c/(2*a)
                r = pow((xc-x1)**2 + (yc-y1)**2,0.5)
                if r == raio:
                    enc = True
                    break
        else:
            continue
        break
    else:
        continue
    break

if(enc):
    print("S")
else:
    print("N")

