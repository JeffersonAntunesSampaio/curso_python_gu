"""
Módulo Collections - Counter (Contador)

Collections -> High-performance Container Datatypes

Counter -> Recebe um interavel como parâmetro e cria um objeto do tipo
Collections Counter que é parecido com um dicionário, contendo como chave o elemento
da lista passada como parâmetro e como o valor a quantidade de ocorrências desse elemento.

"""

from collections import Counter

# Podemos utilizar qualquer iteravel, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Exemplo 1 - Utilizando o Counter
res = Counter(lista)
print(type(res))
print(res)

# Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34: 1})
# Veja que para cada elemento da lista, o counter criou uma chave e colocou como valor a quantidade de ocorrencias

# Exemplo 2
print(Counter("Geek University"))

# Exemplo 3
texto = """
O HMS Agincourt foi um navio couraçado operado pela Marinha Real Britânica. 
Sua construção começou em setembro de 1911 nos estaleiros da Armstrong Whitworth em Newcastle upon 
Tyne e foi lançado ao mar em janeiro de 1913. Era armado com uma bateria 
principal composta por catorze canhões de 305 milímetros montados em sete torres 
de artilharia duplas, o maior número de armas e torres já instalado 
em qualquer couraçado na história. Seu deslocamento era de mais de trinta mil 
toneladas e conseguia alcançar uma velocidade de 22 nós (41 quilômetros por hora).

Foi originalmente encomendado em 1911 pelo Brasil com o nome de Rio de Janeiro, 
parte da corrida armamentista naval da América do Sul. Porém, o colapso 
do ciclo da borracha e melhora nas relações com a Argentina fizeram os 
brasileiros venderem a embarcação para o Império Otomano em dezembro de 1913. 
Foi renomeado como Sultân Osmân-ı Evvel e estava quase completo
"""

palavras = texto.split()
print(palavras)

res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrencias no texo
print(res.most_common(5))
