"""
Dado um número de contatos N e N tuplas de linha onde o primeiro termo é o nome e o segundo o telefone. Crie um dicionario e mostre seu desempilhamento.

Exemplos de Entrada e Saída

Entrada:
4
Yan 1234-5678
Pedro 9999-9999
Ana 8765-4321
Marina 8877-7788

Saída:
('Marina', '8877-7788')
('Ana', '8765-4321')
('Pedro', '9999-9999')
('Yan', '1234-5678')
"""

quant = int(input())

agenda = {}

for i in range(quant):
    nome, tel = input().split()
    agenda[nome] = tel

for i in range(len(agenda)):
    print(agenda.popitem())