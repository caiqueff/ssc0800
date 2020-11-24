"""
Implemente o Diagrama de Classes em anexo

Após isto dado o Nome de um Atleta criar um Objeto do Tipo TriAtleta e print o mesmo

Entrada
Joao

Saida
Corredor Joao correndo
Nadador Joao nadando
Ciclista Joao pedalando
"""

class Atleta:
    def __init__(self, name):
        self.name = name

class Corredor(Atleta):
    def __init__(self, name):
        Atleta.__init__(self, name)

    def correr(self):
        return f"Corredor {self.name} correndo"

class Nadador(Atleta):
    def __init__(self, nome):
        Atleta.__init__(self, nome)

    def nadar(self):
        return f"Nadador {self.name} nadando"

class Ciclista(Atleta):
    def __init__(self, nome):
        Atleta.__init__(self, nome)

    def pedalar(self):
        return f"Ciclista {self.name} pedalando"

class TriAtleta(Corredor, Nadador, Ciclista):
    def __init__(self, name):
        Corredor.__init__(self,name)
        Nadador.__init__(self,name)
        Ciclista.__init__(self,name)

    def __str__(self):
        return f"{self.correr()}\n{self.nadar()}\n{self.pedalar()}"

nome = input()
print(TriAtleta(nome))