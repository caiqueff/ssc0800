"""
Desenvolva um algoritmo que leia uma frase e encontre a maior e a menor palavra nessa frase. Imprima as palavras encontradas. Se houver mais de uma palavra com o menor ou maior tamanho, imprimir a primeira que aparece na frase.

Entrada: Uma frase

Saida: Duas linhas, a menor e a maior palavra, respectivamente

Exemplos de Entrada e Saída

Entrada:
Eu adoro ICC1 por isso programo muito para treinar

Saída:
Eu 
programo

Entrada:
Palavras maiores palavras menores devem imprimir todas

Saída:
devem
Palavras 
"""

palavras = input().split()

tamanhos = [len(palavra) for palavra in palavras]
in_min = tamanhos.index(min(tamanhos))
in_max = tamanhos.index(max(tamanhos))

print(palavras[in_min])
print(palavras[in_max])
