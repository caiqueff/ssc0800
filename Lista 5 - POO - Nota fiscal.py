"""
Lista 5 - POO - Nota fiscal
Faça um programa que realize o cadastro de produtos e gere uma nota fiscal dos produtos comprados. Cada produto possui um código C (inteiro) e seu valor unitário (float). Cada compra contém vários produtos e suas quantidades.

Entrada: A primeira linha da entrada contém o número P (1 <= P <= 50000) de produtos a serem cadastrados. Depois, seguem P linhas, cada uma contendo o código C do produto (1 <= C <= P) e seu preço unitário, separados por espaço. Considere que não há códigos repetidos e eles estão em ordem aleatória. Após isso, a linha seguinte contém o número Q (1 <= Q <= 50000) indicando a quantidade de compras, e as Q linhas seguintes informam, cada uma, o código do produto comprado e sua quantidade; neste caso, os códigos estão em ordem crescente, podendo haver repetições.

O programa deve conter: 1-Uma classe produto 2-Uma classe nota fiscal. 3-Utilizar métodos do tipo get() e set() para acessar atributos de dados dos objetos.

Saída: A saída deverá imprimir a nota fiscal da compra, com cada linha indicando o código do produto, em ordem crescente, sua quantidade total, seu valor unitário e seu valor total. A última linha deverá conter o valor total da nota, conforme os exemplos fornecidos:

Exemplos de Entrada e Saída

Entrada:

4
2 1.99
4 2.03
3 0.95
1 2.19
4
1 1
2 1
2 5
4 2

Saída:

#COD QTD VL_UN R$
#1:    1  2.19 2.19
#2:    6  1.99 11.94
#4:    2  2.03 4.06
Total: R$ 18.19

Entrada:

5
1 2.19
2 1.99
3 0.95
4 2.03
5 0.05
6
1 1
2 1
3 3
4 1
4 1
5 2

Saída:

#COD QTD VL_UN R$
#1:    1  2.19 2.19
#2:    1  1.99 1.99
#3:    3  0.95 2.85
#4:    2  2.03 4.06
#5:    2  0.05 0.10
Total: R$ 11.19
"""
class Produto():
    def __init__(self, codigo, preco):
        self.__codigo = codigo
        self.__preco = preco

    def get_codigo(self):
        return self.__codigo

    def get_preco(self):
        return self.__preco

class Notafiscal():
    def __init__(self, linhas):
        self.__linhas = linhas

    def __str__(self):
        saida = '#COD QTD VL_UN R$\n'
        total = 0
        for c in sorted(self.__linhas):
            qnt = self.__linhas[c]
            if(qnt != 0):
                saida += f'#{c}:    {qnt}  {produtos[c].get_preco():.2f} {produtos[c].get_preco()*qnt:.2f}'
                saida += '\n'
                total += produtos[c].get_preco()*qnt
        saida += f'Total: R$ {total:.2f}'
        return saida

prods = int(input())

produtos = {}
linhas = {}
for i in range(prods):
    c, preco = input().split()
    produtos[int(c)] = Produto(int(c), float(preco))
    linhas[int(c)] = 0

itens = int(input())

for i in range(itens):
    c, quant = input().split()
    linhas[int(c)] += int(quant)

print(Notafiscal(linhas))

