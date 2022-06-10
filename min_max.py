"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elemento.

min() -> Retorna o menor valor em um iterável ou o menor de dois ou mais elementos
"""

# Exemplos

lista = [1, 8, 4, 99, 34, 129]  # Funciona com tuple, set
print(max(lista))  # 129

dicionario = {"a": 1, "b": 8, "c": 4, "d": 99, "e": 34, "f": 129}

print(dicionario)  # {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(dicionario.keys())  # dict_keys(['a', 'b', 'c', 'd', 'e', 'f'])
print(dicionario.values())  # dict_values([1, 8, 4, 99, 34, 129])
print(dicionario.items())  # dict_items([('a', 1), ('b', 8), ('c', 4), ('d', 99), ('e', 34), ('f', 129)])

print(max(dicionario))  # f
print(max(dicionario.values()))  # 129
print(max(dicionario.items()))  # ('f', 129)

print(max(12, 34))  # 34

# Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input("Informe o primeiro valor: "))
val2 = int(input("Informe o segundo valor: "))

print(max(val1, val2))

print(max("a", "ab", "asc"))  # asc

print(max(-454, 485.584, 15.4))  # 485.584


# O min se aplica a todos exemplos a cima


# Outros Exemplos
nomes = ["Arya", "Sanson", "Dora", "Tim", "Ollivander"]

print(max(nomes))  # Tim
print(min(nomes))  # Arya


print(max(nomes, key=lambda nome: len(nome)))  # Ollivander
print(min(nomes, key=lambda nome: len(nome)))  # Tim


musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Dead Skin Mask", "tocou": 2},
    {"titulo": "Back in Black", "tocou": 4},
    {"titulo": "Too old to rock'in'roll", "tocou": 32},
]

print(max(musicas, key=lambda musica: musica["tocou"]))  # {"titulo": "Too old to rock'in'roll", "tocou": 32}
print(min(musicas, key=lambda musica: musica["tocou"]))  # {"titulo": "Dead Skin Mask", "tocou": 2}

# DESAFIO: Imprima somente o titulo da musica mais e menos tocadas
print(max(musicas, key=lambda musica: musica["tocou"])["titulo"])  # Too old to rock'in'roll
print(min(musicas, key=lambda musica: musica["tocou"])["titulo"])  # Dead Skin Mask

# DESAFIO: Como encontrar a musica mais tocada e a menos tocada sem o max(), min() e lambda?

# MAX
musica = {"titulo": "", "tocou": 0}
for line in musicas:
    if line["tocou"] >= musica["tocou"]:
        musica = line

print(musica["titulo"])  # Too old to rock'in'roll

# MIN
musica = {"titulo": "", "tocou": 999999}
for line in musicas:
    if line["tocou"] <= musica["tocou"]:
        musica = line

print(musica["titulo"])  # Dead Skin Mask
