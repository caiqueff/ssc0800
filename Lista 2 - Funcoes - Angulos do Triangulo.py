"""
Desenvolva um programa onde o usuário fornece as medidas dos três ângulos de um triângulo e o tipo de triângulo (agudo, obtuso ou retângulo) é escrito na tela. Lembre-se, você deve verificar também o critério de formação de triângulo, onde a soma dos ângulos internos de um triângulo deve ser 180 graus. Logo, o programa deve ter duas funções: uma função angulotriangulo() que recebe os ângulos e imprime o tipo de triângulo e uma função Ehtriangulo() que recebe os ângulos e retorna 1 se for triangulo e 0, caso contrário.

Dica: Use os seguintes formatadores de print:

print("Triangulo retangulo")
print("Triangulo obtuso")
print("Triangulo agudo")
print ("Valores nao formam um triangulo")
Exemplo de Entrada e Saída

Entrada:
90
45
45

Saída:
Triangulo retangulo
"""

def Ehtriangulo(angs):
    sum = 0
    for i in angs:
        sum+=i
    if(sum == 180):
        return True
    else:
        return False

def angulotriangulo(angs):
    angs.sort()
    maior = angs[-1]
    if maior == 90:
        return "Triangulo retangulo"
    elif maior < 90:
        return "Triangulo agudo"
    else:
        return "Triangulo obtuso"

angulos = []
for i in range(3):
    angulos.append(int(input()))

if(Ehtriangulo(angulos)):
    print(angulotriangulo(angulos))
else:
    print("Valores nao formam um triangulo")