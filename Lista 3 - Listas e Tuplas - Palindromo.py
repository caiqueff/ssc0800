"""
Desenvolva um algoritmo que leia uma sentença e determine se a mesma é ou não é de um palíndromo. Palíndromo: palavras, frases, ou números que preservam seu valor independentemente de serem lidos da esquerda para direita ou da direita para a esquerda. Exemplos: ARARA, AMOR A ROMA, 12321 são palíndromos.

Obs: aqui, não diferenciamos caracteres maiúsculos e minúsculos; 'A' e 'a' são considerados o mesmo caractere.

Entrada: Uma string. A sentença para ser analisada.

Saida: O seu programa deve imprimir "SIM" (sem aspas) se a sentença for um palíndromo e "NAO" caso contrário.

Exemplos de Entrada e Saída

Entrada:
A grama e amarg a

Saída:
SIM

Entrada:
Sorvete no bandejao

Saída:
NAO
"""

frase = input()

for i in range(0,len(frase)):
    if(frase[i].upper() != frase[-i-1].upper()):
        print("NAO")
        break
else:
    print("SIM")
