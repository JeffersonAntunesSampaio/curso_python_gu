"""
Map

Com Map, fazemos mapeamento de valores para função

Map é uma função que reebe dois parâmetros: O primeiro a função, o segundo um iteravel
"""

import math


def area(r):
    """Calcula a área de um circulo com raio 'r'."""
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum
areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# Forma 2 - Map
areas = map(area, raios)

print(areas)
print(type(areas))

print(list(areas))

# Forma 3 - Map com Lambda
areas = map(lambda r: math.pi * (r ** 2), raios)

print(list(areas))  # Primeira utilização = [12.566370614359172, 78.53981633974483, 158.36768566746147, ...]

# OBS: Após utilizar a funcao map() depois da primeira utilização do resultado
# ele zera.
print(list(areas))  # Segunda utilização = []

# Para fixar - Map
# Temos dados iteráveis:
# dados: a1, a2, ....., an
# Temos uma função:
# Função: f(x)
# Utilizamos a funcai map(f, dados) onde map irá mapear cada elemento dos dados e aplicar a função
# Retornará um Map Object


# Mais um exemplo
cidades = [
    ("Berlin", 29),
    ("Cairo", 36),
    ("Buenos Aires", 19),
    ("Los Angeles", 26),
    ("Tokio", 27),
    ("Nova York", 28),
    ("Londres", 22),
]

print(cidades)

# Fórmula de conversão Celsius para Fahrenheit
# f = 9/5 * c + 32

# Lambda
c_para_f = map(lambda dado: (dado[0], round((9/5) * dado[1] + 32)), cidades)

print(list(c_para_f))
