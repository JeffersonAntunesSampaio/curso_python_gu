"""
Funções com Parâmetro (de entrada)

- funções que recebem dados para serem processados dentro da mesma:
- Funções podem ter N parâmetros de entrada, ou seja podemos receber como
entrada de uma função quantos parametros necessários separados por virgula

"""


# Refatorando uma função
def quadrado(numero):
    # return numero * numero
    return numero ** 2  # (**) = Elevar


print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(4)
print(ret)


# Refatorando função 2
def cantar_parabens(aniversariante):
    print("Parabéns para você")
    print("Nesta data querida")
    print("Muitas felicidades")
    print("Muitos anos de vida")
    print(f"Viva o/a {aniversariante}!")


cantar_parabens("Jefferson")


# Exemplo 1
def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 4))
print(multiplica(2, 4))
print(outra(2, 2, "Python "))


# Nomeando parâmetros
def nome_completo(nome, sobrenome):
    return f"Seu nome completo é {nome} {sobrenome}"


print(nome_completo("Jefferson", "Antunes Sampaio"))

# A diferença entre Parâmetros e Argumentos
# Parâmetros são variáveis declaradas na definição de uma função.
# Argumentos são dados passados durante a execução de uma função.

# Argumentos Nomeados (Keyword Arguments)
# Caso utilizemos nomes dos parâmetros nos argumentos para informa-los, podemos
# utilizar qualquer ordem

print(nome_completo(nome="Jefferson", sobrenome="Antunes Sampaio"))
print(nome_completo(sobrenome="Antunes Sampaio", nome="Jefferson"))


# Erro comum na utilização do return
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))
