"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários em
Python são conhecidos por Mapas

Dicionários são coleções de tipo chave/valor.

Dicionários são representados por chaves {}

print(type({}))

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos "chave":"valor".
    - Em dicionários, NÃO podemos ter chaves repetidas
    - Tanto chave quanto valor pode ser de qualquer tipo de dados.
    - Podemos misturar tipo de dados.

"""

# Forma 1 (mais comum)
paises = {
    "br": "Brasil",
    "eua": "Estados Unidos",
    "pg": "Paraguai"
}

print(paises)
print(type(paises))

# Forma 2 (menos comum)
paises = dict(br="Brasil", eua="Estados Unidos", pg="Paraguay")
print(paises)
print(type(paises))

# Acessando elementos do Dicionarios/Mapas
# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print(paises["br"])
print(paises["pg"])

# Forma 2 - Acessando via get - Recomendado
print(paises.get("br"))

# Caso o get não encontre o valor, retorna valor do tipo None
print(paises.get("ru"))

# Caso o get não encontre o valor, podemos definir um valor padrão de retorno
print(paises.get("ru", "VALOR_N_ENCONTRADO"))

# Buscar determinada chave no Dicionario
print("br" in paises)
print("eua" in paises)
print("ru" in paises)

# Podemos utilizar qualquer tipo de dado
# (int, float, string, boolean, list, tuple, dict)

# Tuplas são bastante interessantes de serem utilizadas em chaves de dicionarios, por serem imutaveis.
localidades = {
    (35.6895, 39.6917): "Escritório em Tókio",
    (40.7128, 74.0060): "Escritório em Nova York",
    (37.6895, 122.4194): "Escritório em São Paulo",
}

print(localidades)
print(type(localidades))

# Adicionar elementos em um Dicionario/Mapa
receita = {
    "jan": 100,
    "fev": 120,
    "mar": 300
}

print(receita)
print(type(receita))

# Forma 1 (mais comum)
receita["abr"] = 350
print(receita)

# Forma 2
novo_dado = {"mai": 500}
receita.update(novo_dado)
print(receita)

# Atualizando dados em um dicionário/map

# Forma 1
receita["mai"] = 550
print(receita)

# Forma 2
receita.update({"mai": 600})
print(receita)

# CONCLUSAO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionario é a mesma.
# CONCLUSAO 2: Em dicionários, NÃO podemos ter chaves repetidas


# Remover dados de um dicionário
# Forma 1 (mais comum)
receita.pop("mar")
print(receita)
# OBS 1: Aqui precisamos SEMPRE informar a chave, caso não encontre o elemento,
#       um KEYERROR é retornado
# OBS 2: Ao removermos um objeto, o valor deste objeto é sempre retornado

resp = receita.pop("jan")
print(resp)
print(receita)

# Forma 2 (nessa forma não retorna valor)
del receita["fev"]
print(receita)

# Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras
# no qual adicionamos produtos

"""
Carrinho de Compras:
    Produto 1:
        - nome:
        - quantidade:
        - preço:
    Produto 2:
        - nome:
        - quantidade:
        - preço:
"""

# 1 - Poderiamos utilizar uma lista para isso? Sim
carrinho = []

produto1 = ["Playstation 4", 1, 2800.00]
produto2 = ["God of War 4", 1, 319.99]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# OBS: Nesse modelo teriamos que saber o indice de cada informação no produto.

# 2 - Poderiamos utilizar uma Tupla para isso? Sim

produto1 = ("Playstation 4", 1, 2800.00)
produto2 = ("God of War 4", 1, 319.99)

carrinho = (produto1, produto2)

print(carrinho)

# 3 - Poderiamos utilizar um dicionário para isso? Sim (melhor forma)

carrinho = []

produto1 = {
    "nome": "Playstation 4",
    "quantidade": 1,
    "preço": 2800.00
}

produto2 = {
    "nome": "God of War 4",
    "quantidade": 1,
    "preço": 319.99
}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
# podemos ter a certeza de cada informação

print("------------------------------------------------------------------------------------")

# Métodos de dicionário

d = {
    "a": 1,
    "b": 2,
    "c": 3,
}

print(d)
print(type(d))

# Limpar o dicionário (Zerar dados)
d.clear()
print(d)

# Copiando um dicionário para outro

# Forma 1 # Deep Copy

d = {
    "a": 1,
    "b": 2,
    "c": 3,
}

novo_d = d.copy()

print(novo_d)

novo_d["d"] = 4

print(d)
print(novo_d)

# Forma 1 # Shallow Copy
novo_d = d

print(novo_d)

novo_d["d"] = 4

print(d)
print(novo_d)

# Forma não usual de criação de dicionario
outro = {}.fromkeys("a", "b")
print(outro)
print(type(outro))

usuario = {}.fromkeys(["nome", "pontos", "email", "profile"], "desconhecido")
print(usuario)

# O método fromkeys recebe dois parâmetros: um iterável e um valor
# Ele vai gerar para cada valor iterável uma chave e irá atribuir a esta chave o valor informado.

# Forma 2
veja = {}.fromkeys("testes", "valor")
print(veja)

veja = {}.fromkeys(range(1, 11), "novo")
print(veja)