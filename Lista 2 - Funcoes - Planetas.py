"""
Você, um jovem universitário mochileiro espacial, está viajando pelo sistema solar. Você está com fome e, como todo bom universitário, só tem dinheiro para comer no bandejão.

Portanto, seria muito útil você saber quanto tempo sua viagem até cada um dos planetas durará em termos dos dias de cada planeta, já que cada um tem uma rotação diferente. Assim, você poderia traçar a melhor rota para pegar um bandejão ainda aberto, seja na Terra, em Júpiter, em Vênus ou em Mercúrio (nos outros planetas você sabe que terá picadinho).

Para tanto, você fará um programa que receberá um inteiro contendo o total de segundos gasto na viagem e uma string contendo o nome do planeta de destino.
Então, seu programa deverá calcular quantos dias, horas, minutos e segundos são equivalentes à passagem desse tempo em segundos no planeta destino. Como um bom estudante, você fará uma função que receberá todos esses parâmetros e, calculado o resultado, irá imprimi-lo na main do seu programa.

Vamos arredondar o dia terrestre para 24 horas (você sabe que ele dura 23 horas e 56 minutos, mas os terráqueos gostam de simplificar).
O dia em Vênus equivale a 243 dias terrestres.
O dia em Mercúrio equivale a 58 dias e 16 horas terrestes.
O dia em Júpiter equivale a 9 horas e 56 minutos terrestres (Cuidado, esse vai ser um pouco mais difícil calcular!).
Obs: Todos os nomes de planetas serão fornecidos sem acentos e com a primeira letra maiúscula. Saída desejada:

print(f-'{valor1} segundos no planeta {nomePlaneta} equivalem a:')
print(f-'{valor2} dias, {valor3} horas, {valor4} minutos e {valor5} segundos')

Exemplos de Entrada e Saída

Entrada:
36181 Terra

Saída:
36181 segundos no planeta Terra equivalem a:
0 dias, 10 horas, 3 minutos e 1 segundos

Entrada:
36181 Jupiter

Saída:
36181 segundos no planeta Jupiter equivalem a:
1 dias, 0 horas, 7 minutos e 1 segundos
"""


'''
Sabemos que 24h corresponde a 86400 segundos.

Assim:
O dia em venus equivale a 20995200 segundos terrestres
O dia em mercurio equivale a 5068800 segundos terrestres
O dia em jupiter equivale a 35760 segundos terrestres
'''
segundos, planeta = input().split()
segundos = int(segundos)

def conversor(tempo, planeta):
    tj = 35760
    tm = 5068800
    tv = 20995200

    if planeta == "Jupiter":
        t = tempo
        dias = int(t/tj)
        t -= dias*tj
        horas = int(t/3600)
        t -= horas*3600
        minutos = int(t/60)
        t -= minutos*60
        segundos = t
    if planeta == "Mercurio":
        t = tempo
        dias = int(t/tm)
        t -= dias*tm
        horas = int(t/3600)
        t -= horas*3600
        minutos = int(t/60)
        t -= minutos*60
        segundos = t
    if planeta == "Venus":
        t = tempo
        dias = int(t/tv)
        t -= dias*tv
        horas = int(t/3600)
        t -= horas*3600
        minutos = int(t/60)
        t -= minutos*60
        segundos = t
    if planeta == "Terra":
        t = tempo
        dias = int(t/86400)
        t -= dias*86400
        horas = int(t/3600)
        t -= horas*3600
        minutos = int(t/60)
        t -= minutos*60
        segundos = t
    print(f'{tempo} segundos no planeta {planeta} equivalem a:')
    print(f'{dias} dias, {horas} horas, {minutos} minutos e {segundos} segundos')
conversor(segundos, planeta)
