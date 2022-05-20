"""
Entendendo o *args

- O *args é um parâmetro, como outro qualquer, Isso significa que você poderá
chamar de qualquer coisa, desde que começe com asterisco .

Exemplo:
*xis

Mas por convenção, utilizamos *args para defini-lo

Mas o que é o *args?

O parâmetro *args utilizado em uma função, coloca os valores extrar informados como
entrada em uma tupla. Então desde já lembre-se que tuplas são imutáveis.

"""


# Exemplos

# Função sem *args
def soma_todos_numeros(num1, num2, num3):
    return num1 + num2 + num3


print(soma_todos_numeros(4, 6, 9))


# Função com *args
def soma_todos_numeros_2(*args):
    # Como args é uma tupla, podemos somar com o método sum
    return sum(args)


def soma_todos_numeros_3(nome, sobrenome, *args):
    # fazendo por loop caso tenha tipos de dados diferentes
    total = 0
    for numero in args:
        total += numero
    return total


print(soma_todos_numeros_2())
print(soma_todos_numeros_2(4, 6))
print(soma_todos_numeros_2(4, 6, 9))

print(soma_todos_numeros_3("Angelina", "Jolie"))
print(soma_todos_numeros_3("Angelina", "Jolie", 4, 6))
print(soma_todos_numeros_3("Angelina", "Jolie", 4, 6, 9))


# outro exemplo de utilização de *args
def verifica_info(*args):
    if "Geek" in args and "University" in args:
        return "Bem-vindo Geek"
    return "Eu não tenho certeza quem você é..."


print(verifica_info())
print(verifica_info(1, True, "University", "Geek"))
print(verifica_info(1, "University", 3.145))

# exemplo passando uma lista no argumentos
numeros = [1, 2, 3, 4, 5, 6, 7]

# Usando o * para desempacotar todos itens da lista
print(soma_todos_numeros_2(*numeros))

# OBS: O asterisco serve para que informemos ao Python qu estamos passando
# como argumento uma coleção de dados. Desta forma, ele saberá que
# precisará antes desempacotar esses dados
