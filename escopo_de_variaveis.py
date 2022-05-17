"""
Escopo de variáveis

/                                   /

Dois casos de escopo:
1 - Variáveis globais (seu escopo compreende todo o programa)
2 - Variáveis locaos (seu escopo está limitado ao bloco que foi declarado)
"""

numero = 42
print(numero)
print(type(numero))

"""Python é uma linguagem de tipagem dinâmica. Isso significa que ao
declararmos uma variável, nós não colocamos o tipo de dados dela.
Este tipo é inferido ao atribuimos o valor a mesma
"""
# Reatribuição
numero = 42
print(numero)
print(type(numero))

numero = "numero"
print(numero)
print(type(numero))
