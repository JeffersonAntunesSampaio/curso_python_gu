"""
Mapas -> Conhecidos em Python como Dicionários

Dicionários em Python são representados por chaves {}
"""

receita = {
    'jan': 100,
    'fev': 120,
    'mar': 300,
    'abr': 350
}

print(receita)

# Interar sobre dicionários
for chave in receita:
    print(chave)

# Interar sobre dicionários
for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f"Em {chave} recebi R$ {receita[chave]}")

# Conhecer todas as chaves
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Acessando os valores
print(receita.values())

for valor in receita.values():
    print(valor)

# Desempacotamento de dicionarios
for chave, valor in receita.items():
    print(f"chave={chave} = valor:{valor}")

# Soma, Valor Máximo, Valor Mínimo, Tamanho
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

