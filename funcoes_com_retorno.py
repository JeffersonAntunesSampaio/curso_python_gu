"""
Funções com retorno

Em Python quando uma função não retorna nenhum valor, o retorno é None

OBS: sobre a paralvra reservada return
1 - Ela finaliza a função, ou seja, ela sai da execução da função
2 - Podemos ter, em uma função diferentes returns
3 - Podemos, em uma função retornar qualquer tipo de dado e até mesmo multiplos valores
"""


# Exemplo 1
def quadrado_de_7():
    return 7 * 7


ret = quadrado_de_7()
print(f"Retorno {ret}")


# Refatorando a primeira função
def diz_oi():
    return "oi "


print(diz_oi())

alguem = "Pedro"
print(diz_oi() + alguem)


# Exemplo 2
def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return "b"


print(nova_funcao())


# Exemplo 3
def outra_funcao():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()
print(num1, num2, num3, num4)

# Vamos criar uma função para jogar a moeda
from random import random


def joga_moeda():
    # gera um número pseudo randomico entre 0 e 1
    valor = random()
    if valor > 0.5:
        return "Cara"
    return "Coroa"


print(joga_moeda())


# Erros comuns na utilização do retorno, que na verdade não é erro, mas sim codificação desnecessária
def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    return False


print(eh_impar())
