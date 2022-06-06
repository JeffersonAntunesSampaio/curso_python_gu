"""
Generators Expression

Em aulas anteriores nós estudamos:
- List Comprehension;
- Dict Comprehension;
- Set Comprehension;

Não vimos:
-Tuple Comprehension... porque elas se chama Generators

IMPORTANTE: Gerate são mais performaticos do que List, Dict e Set comprehension
"""

# Generators
nomes = ["Carlos", "Camila", "Carla", "Cassiano", "Cristina", "Vanessa"]

print(any(nome[0] == "C" for nome in nomes))  # Gera um objeto generate


# Qual é a utilizadade de getsizeof() -> Retorna a quantidade de bytes em memória do elemento
# passado como parâmetro

from sys import getsizeof

# mostra quantos bytes a string "geek" está ocupando em memoria. Quanto maior a string, mais espaço ocupa
print(getsizeof("Geek"))

print(getsizeof("University"))

print(getsizeof(9))

print(getsizeof("Geek"))

print(getsizeof(91))

print(getsizeof(9876543214))

print(getsizeof(True))


# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com Dict Comprehension
dict_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de números com Generator
gen = getsizeof(x * 10 for x in range(1000))

print("Para fazer a mesma tarefa gastamos em memória: ")
print(f"List Comprehension: {list_comp} bytes")
print(f"Set Comprehension: {set_comp} bytes")
print(f"Dict Comprehension: {dict_comp} bytes")
print(f"Genarator Expression: {gen} bytes")

# Eu posso iterar no Generator Expression? Sim!
gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)
