""""
Any e All

all() -> Retorna True se todos os elementos do iteravel são verdadeiros
ou ainda se o interavel está vazio

any() -> Retorna True se qualquer elemento do iteravel for verdadeiro.
Se o iteravel estiver vazio, retorna False
"""

# Exemplo all()

print(all([0, 1, 2, 3, 4]))  # Todos os números são verdadeiros? False

print(all([1, 2, 3, 4]))  # Todos os números são verdadeiros? True

print(all([]))  # Iteravel vazio? True

print(all("Geek"))  # Todos os números são verdadeiros? True

nomes = ["Carlos", "Camila", "Carla", "Cassiano", "Cristina"]

print(all([nome[0] == "C" for nome in nomes]))

# Um iteravel vazio convertido para boolean é False, mas no all() entende como True
print(all([letra for letra in "eio" if letra in "aeiou"]))

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))

print(any([0, 1, 2, 3, 4]))  # True

print(any([0, False, {}, (), []]))  # False

nomes = ["Carlos", "Camila", "Carla", "Cassiano", "Cristina", "Vanessa"]

print(any([nome[0] == "C" for nome in nomes]))

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))

print('curso')
