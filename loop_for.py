"""
Loop For

Loop -> Estrutura de repetição
For -> Uma dessas estuturas


"""
nome = "Geek University"  # String
lista = [1, 3, 5, 9]  # Lista
numeros = range(1, 10)  # Tempos que transformar em uma lista

# Exemplo de for 1 (iterando sobre uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (iterando sobre uma lista)
for numero in lista:
    print(numero)

"""
range(valor_inicial, valor_final)
OBS: O valor final não é inclusive
"""

# Exemplo de for 3 (iterando sobre um range)
for numero in range(1, 10):
    print(numero)

"""
Enumerate:
((0,"G"),(1,"e"),(2,"e"),(3,"k")...)
"""
print("--------------------------------------------------------------------")
for indice, letra in enumerate(nome):
    print(nome[indice])

for _, letra in enumerate(nome):
    print(letra)

for valor in enumerate(nome):
    print(valor)

print("--------------------------------------------------------------------")

qtd = int(input("Quantas vezes esse loop deve rodar? "))
soma = 0

for n in range(1, qtd + 1):
    num = int(input(f"Informe o {n}/{qtd} valor: "))
    soma += num
print(f"A soma é {soma}")

print("--------------------------------------------------------------------")

# Original: U+1F60D
# Modificado: U0001F60D

emoji = "U0001F60D"

for x in range(3):
    for num in range(1, 11):
        print("\U0001F60D" * num)

