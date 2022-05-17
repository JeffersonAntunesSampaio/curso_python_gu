"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas.

Existem basicamente duas diferenças básicas:

1 - As tuplas são representadas por parênteses ()
2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda.
    Toda operação em uma tupla gera uma nova tupla.
3 - Métodos para adição e remoção de elementos das tuplas não existem,
    dado o fato que são imutaveis.

Por que utilizar Tuplas
1 - Tuplas são mais rápidas do que lista
2 - TUplas deixam seu código mais seguro (isso porque trabalhar com elementos imutáveis tras segurança ao código)
"""

# CUIDADO 1: As tuplas são representadas por (), mas veja a criação tbm sem os parenteses:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)
print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6  # Também é uma tupla
print(tupla2)
print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento
tupla3 = (4)  # Isso não é uma tupla!!!!
print(tupla3)
print(type(tupla3))

tupla4 = (4,)  # Isso é uma tupla!!!!
print(tupla4)
print(type(tupla4))

tupla4 = 4,  # Isso é uma tupla!!!!
print(tupla4)
print(type(tupla4))

# CONCLUSÃO: Podemos concluir que tuplas são definitas pela virgula
# (4) -> Não é tupla
# (4,) -> É tupla
# 4, -> É tupla

# Podemos gerar uma tupla dinamicamente com range(inicio, fim, passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

# Desempacotamento de tupla
tupla = ("Geek University", "Programação em Python Essencial")
escola, curso = tupla
print(escola, curso)

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
tupla = (1, 2, 3, 4, 5, 6, 8)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas
tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)  # tuplas são imutaveis
print(tupla1)
print(tupla2)

# Tuplas são imutaveis, mas podemos sobrescrever seus valores
tupla1 = tupla1 + tupla2

# Verificar se determiinado  elemento esta contido na tupla
tupla = (1, 2, 3)
print(3 in tupla)

# iterando sobre uma tupla
for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

# Contando elementos dentro de uma tupla
tupla = ("a", "b", "c", "d", "e", "a", "b")
print(tupla.count("a"))

# Convertendo string em uma tupla
escola = tuple("Geek University")
print(escola)
print(escola.count("e"))

# Dicas na utilização de tuplas

# Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos na coleção

# Exemplo 1
meses = (
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
)
print(meses)

# O acesso a elementos de uma tupla também é semelhante a de uma lista
print(meses[5])

# Iterar com while
i = 0

while i < len(meses):
    print(meses[i])
    i += 1

# Verificamos em qual indice um elemento está na tupla
print(meses.index("dezembro"))

# Slicing
# tupla[inicio:fim:passo]
print(meses[0::3])  # trimestre

# Copiando uma tupla para outra
tupla = (1, 2, 3)
outra = (4, 5, 6)
print(tupla)

nova = tupla
outra = nova + outra

print(nova)
print(tupla)
print(outra)
