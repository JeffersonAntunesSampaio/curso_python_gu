"""
PEP8 - Python Enhancement Proposal
São propostas de melhorias para linguagem Python

The Zen of Python
import this
"""

"""
PEP8 Escrever códigos Python de forma Pythonica
"""

"""[1] - Utilize Camel Case para nomes de classes"""


class Calculadora:
    pass


class CalculadoraCientifica:
    pass


"""[2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis"""

numero, numero_impar = 4, 3


def soma():
    pass


def soma_dois():
    pass


"""[3] - Utilize 4 espaços para identação (Não use tab!!!)"""

if "a" in "banana":
    print("tem")

"""
[4] - Separar funções e definições de classe com 2 linhas em branco
    Metodos dentro de uma classe devem ser separados com uma unica linha em branco
"""


class Teste:
    def test(self):
        pass

    def test_2(self):
        pass

    pass


"""[5] - Imports devem ser sempre feitos em linhas separadas.

import sys
import os

# ou

from types import StringType, ListType

# para vários imports

from types import (
    StringType,
    ListType,
    SetType,
)
"""


"""[6] - Espaços em expressões e instruções"""
# funcao(algo[1], {outro: 2})


"""[7] - Termine sempre uma instrução com uma nova linha"""

