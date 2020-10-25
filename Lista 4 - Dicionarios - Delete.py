"""
Dados 3 linhas onde a primeira contem os nomes, a segunda os números de telefones respectivos. Crie uma agenda(dicionario) que relacione o Nome com seu respectivo telefone. Na terceira linha temos nomes de contatos que serão excluídos da agenda. Mostre a agenda(dicionario) resultante apos as remoções.

Exemplos de Entrada e Saída
Entrada:
Joao,Marta,Lis,Hugo,Simoes,Paula,Viviane,Otto,Carlos,Raimundo
169865,4545462,8453,564544,844555,544546,9867,54558,5459,86101
Joao,Simoes,Paula,Carlos,Otto

Saída:
{'Marta': 4545462, 'Lis': 8453, 'Hugo': 564544, 'Viviane': 9867, 'Raimundo': 86101}
"""

nomes = input().split(',')
num = list(map(int, input().split(',')))
nomes2 = input().split(',')
agenda = {}

for i in range(len(nomes)):
    agenda[nomes[i].strip()] = num[i]

for i in nomes2:
    agenda.pop(i)

print(agenda)