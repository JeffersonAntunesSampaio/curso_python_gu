"""
Utilizando Lambdas

Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja,
funções anônimas.

"""


# Função em Python
def funcao(x):
    return 3 * x + 1


print(funcao(4))

# Expressão Lambda
lambda x: 3 * x + 1  # faz exatamente a função de cima

# Como utilizar a expressão lambda (não é a mais comum)
calc = lambda x: 3 * x + 1
print(calc(4))

# Podemos ter expressões lambdas com multiplas entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + " " + sobrenome.strip().title()
print(nome_completo("jefferson    ", "   antunes SAMPAIO"))
# strip() = LTRIM E RTRIM em outras linguagens

# Podemos ter expressões lambdas sem nenhuma entrada
amar = lambda: "Como não amar Python?"

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

# Outro exemplo
autores = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthur C. Clarke", "Frenk Herbert",
           "Orson Scott Card", "Douglas Adams", "h. G. Wells", "Leigh Brackett"]

print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(" ")[-1].lower())
print(autores)


# Função Quadrática
# f(x) = a * x ** 2 + b * x + c

# Definindo a funcao
def geradora_funcao_quadratica(a, b, c):
    """Retorna a função de f(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

# Ou
print(geradora_funcao_quadratica(2, 3, -5)(1))
