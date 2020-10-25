"""
Dado 4 linhas, onde as duas primeiras são os nomes e telefones de uma agenda. E as duas ultimas linhas são os nomes e telefones de uma segunda agenda. Monte um dicionario e mostre em tela a primeira agenda, a segunda agenda e a mesclagem (união[Agenda2 + Agenda1]) da segunda agenda com a primeira.

Exemplos de Entrada e Saída
Entrada:
Joao,Maria,Ana
123,654,897
Pedro,Natalia,Fernanda
456,321,654

Saída:
Agenda 1
{'Joao': 123, 'Maria': 654, 'Ana': 897}
Agenda 2
{'Pedro': 456, 'Natalia': 321, 'Fernanda': 654}
Agenda Mesclada
{'Pedro': 456, 'Natalia': 321, 'Fernanda': 654, 'Joao': 123, 'Maria': 654, 'Ana': 897}
"""

nomes1 = input().split(',')
num1 = list(map(int, input().split(',')))
nomes2 = input().split(',')
num2 = list(map(int, input().split(',')))
agenda1, agenda2, agenda3 = {}, {}, {}

for i in range(len(nomes1)):
    agenda1[nomes1[i].strip()] = num1[i]

for i in range(len(nomes2)):
    agenda2[nomes2[i].strip()] = num2[i]

agenda3.update(agenda2)
agenda3.update(agenda1)

print("Agenda 1")
print(agenda1)
print("Agenda 2")
print(agenda2)
print("Agenda Mesclada")
print(agenda3)