"""
Reduce

OBS: A partir do Python3+ a função reduce() não é mais função integrada (built-in)
Agora temos que importar e utilizar esta funcao a partir do modulo "functools"

Guido van Rossum: Utilize a função reduce se você realmente precisa dela.
Em todo caso, 99% das vezes um loop for é mais legivel.

Para entender o reduce()

# Imagine que vc tem uma coleção de dados:
dados = [a1, a2, a3, .... an]

# E você tem uma função que recebe dois parâmetros:
def funcao(x,y):
    return x * y

A função reduce(), funciona da seguinte forma:
    Passo 1: res1 = f(a1, a2) # Aplica a funcao nos dois primeiros elementos da coleção e guarda o resultado
    Passo 2: res2 = f(res1, a3) # Aplica a funcao passando o resultado do passo1 mais o terceito elemento e guarda o res

    Isso é repedito até o final
    Passo3: res3 = f(res2,a4)

Ou seja, em cada passo ela aplica a função passando como primeiro argumento o resultado da aplicação anterior.
No final o reduce() irá retornar o resultado final

Alternativamente, poderiamos ver a funcao reduce() como:
funcao(funcao(funcao(a1, a2), a3), a4)

"""

# Como funciona na pratica
# Vamos utilizar a função reduce() para multiplicar todos os numeros de uma lista

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]


def multi(x, y):
    return x * y


res = reduce(multi, dados)
print(res)

# Lambda
res = reduce(lambda x, y: x * y, dados)
print(res)


# Utilizando um loop normal

res = 1
for n in dados:
    res = res * n

print(res)

