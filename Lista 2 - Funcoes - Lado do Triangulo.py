"""
Desenvolva um programa onde o usuário fornece as medidas dos três lados de um triângulo e o tipo de triângulo (escaleno, isósceles ou equilátero) é escrito na tela. Lembre-se, você deve verificar também o critério de formação de triângulo, onde um lado qualquer não pode ser maior que a soma dos outros dois. Logo, o programa deve ter duas funções: uma função classificatriangulo() que recebe as medidas e imprime o tipo de triangulo, e uma função Ehtriangulo() que recebe as medidas e retorna 1 se for triangulo e 0, caso contrário.

Dica: Use os seguinte formatadores print:

print("Triangulo Equilatero")
print("Triangulo Isosceles")
print("Triangulo Escaleno")
print ("Valores nao formam um triangulo")
Exemplo de Entrada e Saída

Entrada:
2
3
4

Saída:
Triangulo Escaleno

"""

def Ehtriangulo(a, b, c):
    if(c > (a+b)):
        return 0
    else:
        return 1

def classificatriangulo(a,b,c):
    if(a==b==c):
        return "Triangulo Equilatero"
    elif(a==b or b==c):
        return "Triangulo Isosceles"
    else:
        return "Triangulo Escaleno"

lados = []
for i in range(0,3):
    lados.append(int(input()))
lados.sort()
a, b, c = lados

if not Ehtriangulo(a,b,c):
    print("Valores nao formam um triangulo")
else:
    print(classificatriangulo(a,b,c))
