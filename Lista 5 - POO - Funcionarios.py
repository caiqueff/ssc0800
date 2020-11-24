"""
Implemente o diagrama de Classes representado na imagem em anexo.

Regra 1
Os atributos devem estar privados, logo devem ser definidos com duplo underline __ como mostrado na documentação

Exemplo: _nome ou _codigo

Regra 2
Acessar os atributos/propriedades privados através dos métodos/funções públicos GET e SET

Regra 3
O método get_total_recebido() da classe Funcionário é abstrato e deve ser de declarado e reescrito em suas respectivas heranças

Exercício
Dado um número N de funcionários a serem cadastrados, crie uma lista com estes funcionários que podem ser (1)Clt ou (2)Comissionado

Mostre em tela a lista de funcionários ORDENADA pelo atributo CODIGO

Entrada Modelo
2
1
985
Gabriel Eduardo
Rua 9
900.50
50.20
130.4
2
895
Diane Giovanni
Avenida Principal
600.94
30
12.50
linha 1: N = número de funcionários a serem cadastrados

linha 2: tipo (1 - Clt | 2 - Comissionado)

linha 3: código do funcionário

linha 4: nome do funcionário

linha 5: endereço do funcionário

linha 6: salario base

linha 7: vale transporte | número de vendas

linha 8: vale alimentação | comissão por cada venda realizada

Saída Modelo
Tipo: Comissionado
Nome: Diane Giovanni
Endereco: Avenida Principal
Salario Base: 600.94
Vendas: 30
Comissao: 12.5
Total Recebido: 975.94

Tipo: Clt
Nome: Gabriel Eduardo
Endereco:Rua 9
Salario Base: 900.5
Transporte: 50.2
Alimentacao: 130.4
Total Recebido: 1081.1000000000001
"""
from abc import ABC, abstractmethod


class Pessoa(ABC):
    def __init__(self, codigo, nome, endereco):
        self.__codigo = codigo
        self.__nome = nome
        self.__endereco = endereco

    def get_nome(self):
        return self.__nome
    
    def get_endereco(self):
        return self.__endereco

    def get_codigo(self):
        return self.__codigo

class Funcionario(Pessoa):
    def __init__(self, salario_base):
        self.__salario_base = salario_base

    def get_salario_base(self):
        return self.__salario_base

    @abstractmethod
    def get_total_recebido(self):
        pass

class Clt(Funcionario):
    def __init__(self, codigo, nome, endereco, salario_base, vale_transporte, vale_alimentacao):
        Pessoa.__init__(self, codigo, nome, endereco)
        Funcionario.__init__(self, salario_base)
        self.__vale_transporte = vale_transporte
        self.__vale_alimentacao = vale_alimentacao

    def get_total_recebido(self):
        return self.get_salario_base() + self.__vale_transporte + self.__vale_alimentacao

    def get_vale_transporte():
        return vale_transporte

    def get_vale_alimentacao():
        return vale_alimentacao

    def __str__(self):
        saida = 'Tipo: Clt\nNome: ' + self.get_nome()
        saida += '\nEndereco: ' + self.get_endereco()
        saida += '\nSalario Base: ' + str(self.get_salario_base())
        saida += '\nTransporte: ' + str(self.__vale_transporte)
        saida += '\nAlimentacao: ' + str(self.__vale_alimentacao)
        saida += '\nTotal Recebido: ' +str(self.get_total_recebido())
        return saida + '\n'

class Comissionado(Funcionario):
    def __init__(self, codigo, nome, endereco, salario_base, vendas, comissao):
        Pessoa.__init__(self, codigo, nome, endereco)
        Funcionario.__init__(self, salario_base)
        self.__vendas = vendas
        self.__comissao = comissao

    def get_total_recebido(self):
        return self.get_salario_base() + self.__vendas*self.__comissao

    def get_vendas(self):
        return self.__vendas

    def get_comissao(self):
        return self.__comissao

    def __str__(self):
        saida = 'Tipo: Comissionado\nNome: ' + self.get_nome()
        saida += '\nEndereco: ' + self.get_endereco()
        saida += '\nSalario Base: ' + str(self.get_salario_base())
        saida += '\nVendas: ' + str(self.__vendas)
        saida += '\nComissao: ' + str(self.__comissao)
        saida += '\nTotal Recebido: ' + str(self.get_total_recebido())
        return saida + '\n'

quant = int(input())

pessoas = []
for i in range(quant):
    tipo = input().strip()
    if(tipo == '1'):
        pessoa = Clt(int(input()), input(), input(), float(input()), float(input()), float(input()))
    else:
        pessoa = Comissionado(int(input()), input(), input(), float(input()), int(input()), float(input()))
    pessoas.append(pessoa)

def codigo(pessoa):
    return pessoa.get_codigo()

pessoas.sort(key=codigo)

for i in pessoas:
    print(i)