"""
Modulo Collections - Deque

Podemos dizer que o deque é uma lista de alta performance
"""

# Importa
from collections import deque

# Criando Deque
deq = deque("geek")
print(deq)

# Adicionando elementos no deque
deq.append("y")
print(deq)

deq.appendleft("k")
print(deq)

# Remover elementos
print(deq.pop())  # remove e retorna o ultimo elemento
print(deq)
