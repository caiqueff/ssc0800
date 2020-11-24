"""
Lista 5 - POO - Agenda
Implemente uma agenda com data, hora e atividade a ser realizada, em que data contém, dia, mês e ano e hora contém hora, minuto e segundo. Será passado a quantidade de atividades seguida da data da hora e da atividade. As entradas e saídas deverão ser exibidas de acordo com o exemplo a seguir:

O programa deve conter:

1-Uma classe Agenda.
2-Uma classe Data.
3-Uma classe Hora.
4-Métodos do tipo get() e set() para acessar atributos de dados.

Exemplo de Entrada
3
23
06
2015
23
59
59
Finaliza  entrega  no run.codes
04
07
2015
00
00
01
Inicio  das  Ferias ....=D
13
07
2015
08
15
00
Inicio  da  Recuperacao

Exemplo de Saída
23/06/2015  - 23:59:59
Finaliza  entrega  no run.codes
04/07/2015  - 00:00:01
Inicio  das  Ferias ....=D
13/07/2015  - 08:15:00
Inicio  da  Recuperacao


"""

class Hora:
    def __init__(self, args):
        self.__hora = args[0]
        self.__min = args[1]
        self.__seg = args[2]

    def get_hora(self):
        return f"{self.__hora}:{self.__min}:{self.__seg}"

class Data:
    def __init__(self, args):
        self.__dia = args[0]
        self.__mes = args[1]
        self.__ano = args[2]

    def get_data(self):
        return f"{self.__dia}/{self.__mes}/{self.__ano}"

class Agenda(Hora, Data):
    def __init__(self, data, hora, evento):
        Hora.__init__(self, hora)
        Data.__init__(self, data)
        self.__evento = evento

    def __repr__(self):
        return f'{Data.get_data(self)} - {Hora.get_hora(self)}\n{self.__evento}'

dados = []
for i in range(int(input())):
    data, hora = [], []
    for j in range(3):
        data.append(input())
    for j in range(3):
        hora.append(input())
    evento = input()
    dados.append([data, hora, evento])

eventos = []
for dado in dados:
    eventos.append(Agenda(dado[0], dado[1], dado[2]))

for evento in eventos:
    print(evento)