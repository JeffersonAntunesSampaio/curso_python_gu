"""
Reversed

Reversed funciona com qualquer iterável.
Sua função é inverter o iterável

A função retorna um iterável chamado List Reverse Iterator

OBS: Não confunda com a função reverse() que estudamos nas listas
     A função reverse() só funciona em listas
"""

# Exemplos
lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

# List - Lista
print(list(res))  # [5, 4, 3, 2, 1]
# usando o mesmo res
print(list(res))  # []

# Tuple - Tupla
print(tuple(reversed(lista)))  # (5, 4, 3, 2, 1)

# OBS: Em conjuntos, não definimos a ordem dos elementos
# Set - Conjunto
print(set(reversed(lista)))  # {1, 2, 3, 4, 5}

# Podemos iterar sobre o reversed
for letra in reversed("Geek University"):
    print(letra, end="")  # end="" tira a quebra de linha no final

print("\n")  # pula linha

# Podemos fazer o mesmo sem o uso do for
print("".join(list(reversed("Geek University"))))

# Ja vimos como fazer isso mais facil com slice de strings
print("Geek University"[::-1])

# Podemos tambem utilizar o reversed() para fazer um loop reverso
for n in reversed(range(0, 10)):
    print(n)

# Apesar que também ja vimos como fazer isso utilizando o próprio range()
for n in range(9, -1, -1):
    print(n)

