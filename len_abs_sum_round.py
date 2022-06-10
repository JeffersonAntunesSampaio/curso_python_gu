"""
Len, Abs, Sum, Round


len() -> Retorna o tamanho de um iterável.

abs() -> Retorna o valor absoluto de um numero inteiro ou real.
         De forma básica, seria o seu valor real sem o final

sum() -> Retorna a soma de um iterável.
         Recebe como parâmetro um iterável, podendo recever um valor inicial, e retornar a soma totoal dos elementos.
        OBS: o valor inicial default = 0

round() -> Retorna um número arredondado para "n" digito de precisão após a casa decimal.
           Se a precisão não for informada, retorna o inteiro mais próximo da entrada
"""

# Exemplos Len
print(len("Geek Universety"))
print(len([1, 2, 3, 4, 5]))
print(len((1, 2, 3, 4, 5)))
print(len({1, 2, 3, 4, 5}))
print(len({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5,}))
print(len(range(0, 10)))

# Por debaixo dos panos, quando utilizamos a função len() o Python faz o seguinte:

# Dunder len - "__"
print("Geek University".__len__())

# Exemplos Abs
print(abs(-5))  # 5
print(abs(3))  # 3
print(abs(3.14))  # 3.14
print(abs(-3.14))  # 3.14

# Exemplos Sum
print(sum([1, 2, 3, 4, 5]))  # 15
print(sum([1, 2, 3, 4, 5], 5))  # 20
print(sum([1, 2, 3, 4, 5], -5))  # 10


# Exemplos Round
print(round(10.2))  # 10
print(round(10.5))  # 10
print(round(10.6))  # 11
print(round(1.582121584, 2))  # 1.58
print(round(1.9999999, 2))  # 2.0
