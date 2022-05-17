"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência a
Teoria dos Conjuntos da Matemática

- Aqui no Python, os conjuntos sçai chamados de Sets.

Dito isto, da mesma forma que na matemática:
 - Sets (conjuntos) não possuem valores duplicados
 - Sets (conjuntos) não possuem valores ordenados
 - Elementos não são acessados via indice, ou seja, conjuntos não são indexados
 - Importante lembrar que além de não termos valores duplicados, não temos ordem
Conjuntos são bons para se utilizar quando precisamos armazenar elementos, mas
não nos importamos com a ordenção deles. Quando não precisamos se preocupar
com chaves, valores e itens duplicados

Os conjuntos (sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos (Set) e Mapas (Dicionários) em Python:
    - Um dicionario tem chave/valor
    - Um conjunto tem apenas valor
"""

# Definindo um conjunto
# Forma 1
s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})
print(s)

# Forma 2 (mais comum)
s = {1, 2, 3, 4, 5, 5}
print(s)

# Podemos verificar se o determinado elemento possui no conjunto
if 3 in s:
    print("Tem o 3")
else:
    print("Não tem o 3")

# Importante lembrar que além de não termos valores duplicados, não temos ordem
dados = [12, 10, 2, 2, 5, 6, 7, 7]

# Listas aceitam valores duplicados (guarda a ordem que foi inserida)
lista = list(dados)
print(f"Lista: {lista} com {len(lista)} elementos")

# Tuplas aceitam valores duplicados (guarda a ordem que foi inserida)
tupla = tuple(dados)
print(f"Tuplas: {tupla} com {len(tupla)} elementos")

# Dicionários NÃO aceitam valores duplicados (guarda a ordem que foi inserida)
dicionario = {}.fromkeys(dados, "dict")
print(f"Dicionário: {dicionario} com {len(dicionario)} elementos")

# Conjutos NÃO aceitam valores duplicados (faz uma ordenação propria)
conjunto = set(dados)
print(f"Conjunto: {conjunto} com {len(conjunto)} elementos")

# Assim como todo outro conjuto Python podemos colocar tipo de dados misturados em Sets
s = {1, "b", True, 34.22, 44}
print(s)
print(type(s))

# podemos iterar em um SET normalmente
for valor in s:
    print(valor)

# Usos interessantes com sets
# Imagine que fizemos um formulario de cadastro de visitantes em uma feira ou museu
# e os visitantes informam manualmente a cidade de onde vieram
# Nos adicionamos cada cidade em uma lista Python, ja que em uma lista podemos adicionar novos elementos
# e ter repetição

cidades = [
    "Belo Horizonte",
    "São Paulo",
    "Campo Grande",
    "Cuiaba",
    "Campo Grande",
    "São Paulo",
    "Cuiaba"
]

# Quantas pessoas visitaram o museu?
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja, únicas, temos.
# O que você faria? Faria um loop na lista?
# podemos utilizar o set para isso!
print(len(set(cidades)))

# Adicionando um elemento em um conjunto
s = {1, 2, 3}
print(s)

s.add(4)
print(s)

# Remover elemento de um conjunto
# Forma 1
s.remove(3)  # Não é indice, informamos o valor removido
print(s)

# Forma 2
s.discard(2)  # Não é indice, informamos o valor removido
print(s)

# Copiando um conjunto para outro...
# Forma 1 - Deep Copy
novo = s.copy()
print(novo)

novo.add(8)

print(novo)
print(s)

# Forma 2 - Shallow Copy
novo = s
print(novo)

novo.add(8)

print(novo)
print(s)

# Podemos remover todos os itens de um conjunto
s.clear()
print(s)

# Métodos Matemáticos de Conjutos

# Imagine que temos dois conjuntos: um contento estudantes do curso Python e
# um contento estudantes do curso Java

estudantes_python = {
    "Marcos",
    "Patricia",
    "Ellen",
    "Pedro",
    "Julia",
    "Guilherme",
}

estudantes_java = {
    "Fernando",
    "Gustavo",
    "Julia",
    "Ana",
    "Patricia",
}

# Veja que alguns alunos que estudam Python também estudam Java

# Precisamos gerar um conjunto com nomes de estudantes unicos

# Forma 1 - Utilizando union
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - Utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando &
ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar resultado de estudantes que não estão no outro curso
so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# Soma, Valor Máximo, Valor Minímo, Tamanho
s = {1, 2, 3, 4, 5, 6, }

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
