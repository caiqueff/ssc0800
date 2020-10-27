"""
Desenvolva um algoritmo que leia um número representando um ângulo qualquer entre 0º e 360º, calcule e escreva seu correspondente em radianos (rad = PI*angulo/180).

Entrada: Um número real (angulo), sendo 0 <= angulo <= 360.

Saída: Um número real representando o valor do ângulo em radianos impresso com 6 casas decimais.

Dica 1: Para PI, utilize math.pi,
Dica 2: inclua import math no início do seu código
Dica 3: arredondar em 6 casas decimais usando round( valor,6)

Exemplos de Entrada e Saída
Entrada:
0
Saída:
0.0

Entrada:
180
Saída:
3.141593

# comentario 
"""
import math

angulo = float(input())

rad = round(math.pi*angulo/180, 6)
print(rad)
