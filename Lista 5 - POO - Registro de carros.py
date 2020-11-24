"""
Lista 5 - POO - Registro de carros
Criar uma classe para carros com as seguintes informações: id, fabricante, modelo, ano, cor, preço. Em seguida, implemente um programa que ofereça ao usuário as seguintes operações:
1. Ler os dados de um carro.
2. Buscar um determinado carro por meio de seu ID e imprimir seus dados (operação 1)
3. Modificar o fabricante para "GM" caso o registro seja Chevrolet (operação 2)
4. Imprimir os dados de todos os carros (operação 3)

Os campos fabricante, modelo e cor não terão mais de 20 caracteres. O primeiro valor a ser fornecido, será o da quantidade de carros a ser cadastrada e, em seguida, os dados de cada um. A entrada e saída do seu programa devem ser de acordo com os exemplos abaixo:

Exemplo de entrada
2
123
Chevrolet
Passat
Preto
2004
20000
456
Toyota
Corolla
Preto
2003
30000
1
123
2
3
1
456
0
Note que a operação zero deverá finalizar o programa.

Exemplo de saída
Fab: Chevrolet
Mod: Passat
Cor: Preto
Ano: 2004
Pre: 20000

Fab: GM
Mod: Passat
Cor: Preto
Ano: 2004
Pre: 20000

Fab: Toyota
Mod: Corolla
Cor: Preto
Ano: 2003
Pre: 30000

Fab: Toyota
Mod: Corolla
Cor: Preto
Ano: 2003
Pre: 30000

"""


class Carro:
    def __init__(self, args):
        self.__id = args[0]
        self.__fabricante = args[1]
        self.__modelo = args[2]
        self.__cor = args[3]
        self.__ano = args[4]
        self.__preco = args[5]
    
    def get_id(self):
        return self.__id

    def get_fab(self):
        return self.__fabricante

    def get_registro(self):
        return f'Fab: {self.__fabricante}\nMod: {self.__modelo}\nCor: {self.__cor}\nAno: {self.__ano}\nPre: {self.__preco}'

    def set_fab(self, fab):
        self.__fabricante = fab

def busca_id(carros, id):
    for carro in carros:
        if carro.get_id() == id:
            return f'{carro.get_registro()}\n\n'

def buscar_todos(carros):
    retorno = ''
    for carro in carros:
        retorno += f'{carro.get_registro()}\n\n'
    return retorno

carros = []

for i in range(int(input())):
    carro = []
    for j in range(6):
        carro.append(input())
    carros.append(Carro(carro))

imprimir = ''
while True:
    opcao = input().strip()
    if opcao == '1':
        imprimir += f'{busca_id(carros, input().strip())}'
    elif opcao == '2':
        for carro in carros:
            if carro.get_fab() == 'Chevrolet':
                carro.set_fab('GM')
    elif opcao == '3':
        imprimir += f'{buscar_todos(carros)}'
    elif opcao == '0':
        break

print(imprimir.strip(), end='\n\n')