"""
Lista 5 - POO - Básico - Gerenciamento de estudantes
Desenvolva um código capaz de gerenciar registros de alunos de uma universidade. Cada registro é composto por quatro campos:
identificador, nome, curso e idade. Seu programa deve ser capaz de:

Ler n registros até que o usuário forneça -1
Ler n operações até que o usuário forneça -1
Permitir que um aluno seja consultado por meio de seu identificador e que seu registro seja impresso caso esta operação seja selecionada (operação 1)
Permitir a consulta de todos os alunos de um determinado curso e impressão de seus registros (operação 2)
Permitir que todos os registros armazenados sejam impressos (operação 3)
O código deve obrigatoriamente conter:
1- Uma classe Aluno.
2- Armazenar os objetos gerados pela classe Aluno em uma lista.
3- Utilizar métodos do tipo get() e set() para acessar os atributos de dados do objeto.

Códigos desenvolvidos sem utilizar POO serão desconsiderados.

Exemplos de entrada

9297384
Fulano da Silva
Ciencias da Computacao
20
8237381
Fulano da Silva Segundo
Ciencias da Computacao
22
9787485
Fulano da Silva Terceiro
Sistemas de Informacao
20
6578309
Fulano da Silva Diferentoso
Arquitetura e Urbanismo
23
-1
1
9297384
2
Ciencias da Computacao
3
-1

Exemplo de Saída

Nome: Fulano da Silva
Curso: Ciencias da Computacao
N USP: 9297384
Idade: 20

Nome: Fulano da Silva
Curso: Ciencias da Computacao
N USP: 9297384
Idade: 20

Nome: Fulano da Silva Segundo
Curso: Ciencias da Computacao
N USP: 8237381
Idade: 22

Nome: Fulano da Silva
Curso: Ciencias da Computacao
N USP: 9297384
Idade: 20

Nome: Fulano da Silva Segundo
Curso: Ciencias da Computacao
N USP: 8237381
Idade: 22

Nome: Fulano da Silva Terceiro
Curso: Sistemas de Informacao
N USP: 9787485
Idade: 20

Nome: Fulano da Silva Diferentoso
Curso: Arquitetura e Urbanismo
N USP: 6578309
Idade: 23

Note que cada registro é separado por dois pulos de linha e que o -1 é utilizado para indicar o fim da entrada de registros e, também de operações. Caso o aluno buscado não seja encontrado, seu programa deverá imprimir "Aluno nao cadastrado", seguido por uma quebra de linha

"""


class Aluno:
    def __init__(self, args):
        self.__id = args[0]
        self.__nome = args[1]
        self.__curso = args[2]
        self.__idade = args[3]
    
    def get_id(self):
        return self.__id

    def get_curso(self):
        return self.__curso

    def get_registro(self):
        return f'Nome: {self.__nome}\nCurso: {self.__curso}\nN USP: {self.__id}\nIDADE: {self.__idade}'

def busca_id(pessoas, id):
    for pessoa in pessoas:
        if pessoa.get_id() == id:
            return f'{pessoa.get_registro()}\n\n'
    else:
        return 'Aluno nao cadastrado'

def busca_curso(pessoas, curso):
    retorno = ''
    for pessoa in pessoas:
        if pessoa.get_curso() == curso:
            retorno += f'{pessoa.get_registro()}\n\n'
    return retorno

def buscar_todos(pessoas):
    retorno = ''
    for pessoa in pessoas:
        retorno += f'{pessoa.get_registro()}\n\n'
    return retorno

dados = []

while True:
    dado = input().strip()
    dados.append(dado)
    if dado == '-1':
        dados.pop()
        break

pessoas = [[dados[i], dados[i+1], dados[i+2], dados[i+3]] for i in range(0,len(dados),4)]
pessoas = [Aluno(pessoa) for pessoa in pessoas]

imprimir = ''
while True:
    opcao = input().strip()
    if opcao == '1':
        imprimir += f'{busca_id(pessoas, input().strip())}'
    elif opcao == '2':
        imprimir += f'{busca_curso(pessoas, input().strip())}'
    elif opcao == '3':
        imprimir += f'{buscar_todos(pessoas)}'
    elif opcao == '-1':
        break

print(imprimir.strip(), end='\n\n')