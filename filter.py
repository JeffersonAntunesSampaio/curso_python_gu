"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção
"""
# Biblioteca para trabalhar com dados estatistics
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(f"Média: {media}")

res = filter(lambda x: x > media, dados)
print(list(res))

# Outro exemplos

paises = ["", "Argentina", "", "Brasil", "Chile", "", "Colombia", "", "Equador", "", "", "Venezuela"]
print(paises)

# None no filter automaticamente tira os dados vazios
res = filter(None, paises)
print(list(res))

# A diferença entre map() e filter() é:
# map() -> Recebe dois parâmetros, uma função e um iterável e
# retorna um objeto mapeando a função para cada elemento do iterável
# filter() -> Recebe dois parâmetros, uma função e um iteravel e
# retorna um objeto filtrado de acordo com o retorno da função (True, False)

# Exemplo mais complexo
usuarios = [
    {
        "username": "samuel",
        "tweets": [
            "Eu adoro bolos",
            "Eu adoro pizzas",
        ],
    },
    {
        "username": "carla",
        "tweets": [
            "Eu amo meu gato",
        ],
    },
    {
        "username": "jeff",
        "tweets": [],
    },
    {
        "username": "bob123",
        "tweets": [],
    },
    {
        "username": "doggo",
        "tweets": [
            "Eu gosto de cachorros",
            "Vou sair hoje",
        ],
    },
    {
        "username": "gal",
        "tweets": [],
    },

]

print(usuarios)

# Filtrar os usuários que estão inativos no twitter

# Forma 1
inativos = list(filter(lambda usuario: len(usuario["tweets"]) == 0, usuarios))
print(inativos)

# Forma 2
inativos = list(filter(lambda usuario: not usuario["tweets"], usuarios))
print(inativos)


# Combinar filter() e map()
nomes = ["Vanessa", "Ana", "Maria"]

# Devemos criar uma lista contendo "Sua instrutura é" + nome, desde que cada nome tenha menos de 5 caracteres
lista = list(map(lambda nome: f"Sua instrutora é {nome}", filter(lambda nome: len(nome) < 5, nomes)))
print(lista)
