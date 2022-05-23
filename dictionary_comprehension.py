"""
Dictionary Comprehesion

Pense no seguinte:

Se quisermos criar uma lista fazemos:

lista = [1, 2, 3, 4]

Se quisermos criar uma tupla:

tupla = (1, 2, 3, 4)

Se quisermos criar um set (conjunto):

conjunto = {1, 2, 3, 4}

Se quisermos criar um dicionário:

dicionario = {"a": 1, "b": 2, "c": 3, "d": 4}

# Sintaxe

{chave: valor for chave,valor in iteravel}
"""

# Exemplos

numeros = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print(numeros)

quadrados = {chave: valor ** 2 for chave, valor in numeros.items()}
print(quadrados)

# Exemplo 2
numeros = [1, 2, 3, 4, 5]

quadrados = {valor: valor ** 2 for valor in numeros}
print(quadrados)

# Exemplo 3
chaves = "abcde"
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# Exemplo 4 com lógica condicional
numeros = [1, 2, 3, 4, 5, 6]

res = {num: ("par" if num % 2 == 0 else "impar") for num in numeros}
print(res)
