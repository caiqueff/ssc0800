"""
Dados 3 linhas onde a primeira linha temos os nomes do correntistas, na segunda seus respectivos saldos. Monte um dicionario vinculando a Pessoa com seu Saldo atual. Na terceira linha temos alguns nomes de clientes que serão pesquisados pelo gerente, caso o nome seja de um cliente cadastrado mostre seu saldo caso contrário mostre "Nao Cadastrado" em tela

Exemplos de Entrada e Saída

Entrada:
Joao,Marta,Lis,Hugo,Simoes,Paula,Viviane,Otto,Carlos,Raimundo
165,4562,8453,564,8455,5446,9867,558,5459,86101
Joao,Fernando,Paloma,Marta,Mariana

Saída:
165
Nao Cadastrado
Nao Cadastrado
4562
Nao Cadastrado
"""

nomes = input().split(',')
valores = input().split(',')
consulta = input().split(',')

contas = {}

for i in range(len(nomes)):
    contas[nomes[i]] = valores[i]

for j in range(len(consulta)):
    print(contas.get(consulta[j], 'Nao Cadastrado'))