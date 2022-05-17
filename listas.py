"""
Listas

Listas em Python funciona como vetores/matrizes (arrays) em outras linguagens, com a diferença
de serem DINÂMICO e também de podermos colocar em QUALQUER tipo de dado.

Linguagens C/Java: Arrays
    - Possui tamanho e tipo de dado fixo.

Em Python
- Dinâmico: Não possui tamanho fixo.
- Qualquer tipo de dado.
- Listas são representadas por colchetes []
- Lista são mutáveis, podem alterar constantemente
"""

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ["G", "e", "e", "k", " ", "U", "n", "i", "v", "e", "r", "s", "i", "t", "y"]

lista3 = []

lista4 = list(range(11))

lista5 = list("Geek Universoty")

# Podemos facilmente checar se determinado valor está na lista
num = 1
if num in lista4:
    print(f"Encontei o número {num}")
else:
    print(f"Não encontrei o número {num}")

# Podemos facilmente ordernar uma lista
lista1.sort()
print(lista1)

# Podemos contas quantidade de items em uma lista
print(len(lista1))

# Podemos facilmente contar o número de ocorrências de um valor em uma lista
print(lista1.count(1))
print(lista5.count("e"))

# Adicionar elementos em listas
"""
Para adicionar elementos em listas, utilizamos a função append
OBS: Com append, nós só podemos adicionar um elemnto por vez
"""
print(lista1)
lista1.append(42)
print(lista1)

# Incluir mais de um elemento na lista
lista1.extend([215, 44, 57])  # Coloca cada elemento da lista como valor adicional
print(lista1)

lista1.append([5, 8, 1])  # Coloca a lista como elemento
print(lista1)

if [5, 8, 1] in lista1:
    print("Encontrei a lista")
else:
    print("Não encontrei a lista")

# Podemos inserir um novo elemento da lista informando a posição do indice
lista1.insert(0, "Novo valor")
print(lista1)

# Podemos facilmente juntar duas listas
lista6 = lista1 + lista2
print(lista6)

# Podemos facilmente inverter uma lista
lista1.reverse()
# OU print(lista1[::-1])
lista2.reverse()
# OU print(lista2[::-1])

print(lista1)
print(lista2)

# Copiar uma lista
lista7 = lista2.copy()
print(lista7)

# Tamanho da lista
print(len(lista6))

# Podemos remover facilmente o ultimo elemento da lista
print(lista5)
lista5.pop()  # POP remove o ultimo elemento e tbm retorna o elemento que removeu
print(lista5)

# Podemos remover um elemento pelo indice
lista5.pop(2)
print(lista5)

# Podemos remover todos elementos
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente transformar string para uma lista
curso = "Curso da Geek University"
print(curso)
curso = curso.split()
print(curso)

# Convertendo uma lista em uma string
lista8 = ["Programação", "em", "Python", "Essencial"]
print(lista8)
curso1 = ' '.join(lista8)
print(curso1)

# Diferentes tipos de dados na mesma lista
lista9 = [1, 2.34, True, "Geek", "d", [1, 2, 3], 45632158748]

# Iterando sobre lista
# Exemplo 1 com for
for elemeto in lista9:
    print(elemeto)

# Exemplo 2 com While
carrinho = []
produto = ""

while produto != "sair":
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != "sair":
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Fazemos acesso aos elementos de forma indexadas
cores = ["verde", "amarelo", "azul", "branco"]
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])
print(cores[-1])
print(cores[-2])
print(cores[-3])
print(cores[-4])

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice += 1

# Gerar indice em um for
for indice, cor in enumerate(cores):
    print(indice, cor)

# Outros métodos não tão importantes mas também úteis

# Encontrar o indice e um elemento na lista
numeros = [5, 6, 7, 8, 9, 10]

# Em qual indice da lista esta o valor 6
# index retorna o primeiro indice do numero que achar
print(numeros.index(6))

# Em qual indice da lista esta o valor 6
print(numeros.index(9))

# Caso não tenha o numero da lista, retorna erro
# print(numeros.index(19))

# Podemos fazer uma busca dentro de um range, ou seja, qual indice começar a buscar
print(numeros.index(6, 1))

# numeros.index(valor_buscado, indice inicial, indice_final)
print(numeros.index(6, 1, 3))

# Revisão de slicing
# lista[inicio:fim:passo]
# range[inicio:fim:passo]

lista10 = [1, 2, 3, 4]

# Iniciando no indice 1 e pegando todos os elementos restantes
print(lista10[1:])

# Começa em 0, pega até o indice 2 - 1
print(lista10[:2])

# Iniciando no indice 1 e pegando todos os elementos restantes pulando de 2 em 2
print(lista10[1::2])

# Invertendo valores em uma lista

nomes = ["Geek", "University"]
nomes[0], nomes[1] = nomes[1], nomes[0]

# Ou
print(nomes.reverse())

# Somar, Valor Maximo, Valor Minimo, Tamanho de lista
lista11 = [1, 2, 3, 4, 5, 6]

print(sum(lista11))  # soma
print(max(lista11))  # máximo valor
print(min(lista11))  # mínimo valor
print(len(lista11))  # tamanho da lista

# Transformar lista em tupla
tupla = tuple(lista11)
print(tupla)
print(type(tupla))

# Desempacotamento de listas
num1, num2, num3, num4, num5, num6 = lista11  # Lembrar de colocar a mesma quantidade de elementos

print(num1, num2, num3, num4, num5, num6)

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Exemplo 1 #### Deep Copy #####
lista12 = [1, 2, 3]
print(lista12)

# Copy -  Copiar os items para nova lista, porém se tornam independentes
# Isso em Python é chamado em Deep Copy (copia profunda)
nova = lista12.copy()
print(nova)
nova.append(4)

print(lista12)
print(nova)

# Exemplo 2 #### Shallow Copy #####
# Cria como se fosse um ponteiro de uma lista

lista12 = [1, 2, 3]
print(lista12)

# Atribuição da lista -  Copiar os items para nova lista, porém ao realizar uma alteração ela reflete na nova lista
# Isso em Python é chamado em Shallow Copy
nova = lista12  # Copia via atribuição
print(nova)
nova.append(4)

print(lista12)
print(nova)
