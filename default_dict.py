"""
Modulo Collections - Default Dict

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default
podendo utilizar um lambda para isso. Esse valor será utilizado sempre que não houver um valor definido.
Caso tentamos acessar uma chave que não existe, essa chave será criada e o valor default será atribuido


OBS: Lambdas são funções sem nome, que podem ou não receber parâmetros de entrada
e retornar valores

"""

# Recap Dicionario
dicionario = {
    "curso": "Programação em Python"
}

print(dicionario)
print(dicionario["curso"])

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario["curso"] = "Programação em Python: Essencial"

print(dicionario)
print(dicionario["outro"])
print(dicionario)
