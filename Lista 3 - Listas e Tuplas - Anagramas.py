"""
Dadas N strings, determinar quantos anagramas existem para cada uma. Entrada: Um inteiro positivo N; em seguida, N linhas, cada uma contendo uma string de carácteres alfabéticos minúsculos, seguidas de uma quebra de linha (‘\n’) Saída: N linhas, cada uma contendo um inteiro que representa a quantidade de anagramas; a i-ésima linha impressa é a resposta para a i-ésima string inserida, com i de 1 até n.

Exemplos de Entrada e Saída

Entrada
5
banana
poo
aaaaaa
paralelepipedo
urubu

Saída
60
3
1
605404800
20

“How happy is the blameless vestal’s lot!
The world forgetting, by the world forgot.
Eternal sunshine of the spotless mind!
Each pray’r accepted, and each wish resign’d”


"""

qnt = int(input())

termos = []
for i in range(qnt):
    termos.append(input().strip())

def count(palavra):
    letras = []
    for i in range(len(palavra)):
        if palavra[i] not in letras:
            letras.append(palavra[i])
    den = 1
    for letra in letras:
        qnt = palavra.count(letra)
        den *= fatorial(qnt)
    return(int(fatorial(len(palavra))/den))

def fatorial(num):
    fat = 1
    for i in range(1,num+1):
        fat *= i
    return fat

caracs = [count(palavra) for palavra in termos]

for i in caracs:
    print(i)
