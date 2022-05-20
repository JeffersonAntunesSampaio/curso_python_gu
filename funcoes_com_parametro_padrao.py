"""
Funções com Parâmetros Padrão (Default Paramters)

- Funções onde a passagem de parâmetro seja opnicional
- Funções com parâmetros default (padrão), deve estar no final da declaração
"""


# Exemplo 1 (obrigatório)
def quadrado(numero):
    return numero ** 2


print(quadrado(4))


# Exemplo 2 (opcional)
def exponencial(numero, potencia=2):
    return numero ** potencia


print(exponencial(2, 4))
print(exponencial(4))  # Por padrão eleva ao quadrado
print(exponencial(4, 4))


# Exemplo mais complexo
def mostra_informacao(nome="Geek", instrutor=False):
    if nome == "Geek" and instrutor:
        return "Bem vindo instrutor Geek!"
    elif nome == "Geek":
        return "Eu pensei que você era o instrutor"
    return f"Olá {nome}"


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(nome="Ozzy"))


# Exemplo com função como parametro
def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(3, 2))
print(mat(3, 2, subtracao))

# Escopo- Evitar problemas e confusões...

# Variáveis globais
# Variaveis locais

instrutor = "Geek"  # Variavel global


# Se tivermos uma variável local com o mesmo nome de uma global,
# a local terá preferencia
def diz_oi():
    instrutor = "Python"  # Variável loca
    return f"Oi {instrutor}"


print(diz_oi())


def diz_ola():
    prof = "Python 2"  # Variável loca
    return f"Olá {prof}"


print(diz_ola())

# ATENCAO com variáveis globais (Se puder evitar, evite!)

# Como utilizar uma global dentro de uma função

total = 0


def incrementa():
    global total  # Avisando que queremos utilizar a global

    total = total + 1
    return total


print(incrementa())


# Podemos ter funções que são declaradas dentro de funções e
# também tem uma forma especial de escopo de variável (n comum)


def fora():
    contator = 0

    def dentro():
        nonlocal contator  # Forma Não comum
        contator = contator + 5
        return contator

    return dentro()


print(fora())
