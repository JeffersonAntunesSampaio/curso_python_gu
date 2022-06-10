"""
Zip

zip() -> Cria um iterávell (Zip Object) que agrega elemento de cada um dos iteráveis
passados como entrada em pares

"""

# Exemplos
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip1))

# List
print(list(zip1))  # [(1, 4), (2, 5), (3, 6)]

# Tuple
print(tuple(zip(lista1, lista2)))  # ((1, 4), (2, 5), (3, 6))

# Set
print(set(zip(lista1, lista2)))  # {(2, 5), (1, 4), (3, 6)}

#Dict
print(dict(zip(lista1, lista2)))  # {1: 4, 2: 5, 3: 6}

# Uniao da listq
print(lista1 + lista2)  # [1, 2, 3, 4, 5, 6]

lista3 = [7, 8, 9, 10, 11]

# OBS: O zip() utiliza como parâmetro o menor tamanho em iteravel.
# Se tiver trabalhando com tamanhos diferentes, irá parar quando o menor acabar
zip1 = zip(lista1, lista2, lista3)

print(list(zip1))  # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]

# Podemos utilizar diferentes iteráveis com zip
tupla = 1, 2, 3, 4, 5,
lista = [6, 7, 8, 9, 10,]
dicionario = {"a": 11, "b": 12, "c": 13, "d": 14, "e": 15}
conjunto = {16, 17, 18, 19, 20}

z1 = zip(tupla, lista, dicionario.values(), conjunto)
print(list(z1))  # [(1, 6, 11, 16), (2, 7, 12, 17), (3, 8, 13, 18), (4, 9, 14, 19), (5, 10, 15, 20)]

# Lista de tuplas
dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

# Usando desempacotamento
print(list(zip(*dados)))  # [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]

# Exemplos mais complexos
prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ["maria", "pedro", "carla"]

print(list(zip(alunos, prova1, prova2)))  # [('maria', 80, 98), ('pedro', 91, 89), ('carla', 78, 53)]

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}
print(final)  # {'maria': 98, 'pedro': 91, 'carla': 78}

# Podemos utilizar o man
final = dict(zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2))))
print(final)