"""
Utilizando uma série de Taylor , o seno de um ângulo pode ser calculado aproximação encontrada na imagem em anexo, sendo x um ângulo em radianos (no primeiro quadrante do círculo trigonométrico).

Faça um programa que leia o ângulo x (número real) e a quantidade de iterações que se deve fazer para encontrar o seno. Seu programa deverá ter duas funções: uma para calcular o fatorial de um número e a outra para calcular o valor do seno de x. Na saída, o resultado deverá ter 6 casas decimais

Dica1: print('%.6f'%seno_valor) Dica2: Converta o valor que armazena fatorial para float - fat=i*float(fat) - isso evitará problemas com overflow!!!

Exemplos de Entrada e Saída

Entrada:
0.785398 300

Saída:
0.707107
"""

def fatorial(n: int):
    fat = float(1)
    for i in range(1, n+1):
        fat *= float(i)
    return fat

def sen(x: float, inter: int):
    sin = float(0)
    for i in range(1, inter+1):
        sin += float(pow(-1, i+1)*pow(x, 2*i - 1)/fatorial(2*i - 1))
    return sin
        
valores = input().split()
seno = sen(float(valores[0]), int(valores[1]))
print('%.6f'%seno)
