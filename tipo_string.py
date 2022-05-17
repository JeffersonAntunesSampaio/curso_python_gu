"""
Tipo string

Em Python, um dado é considerado do tipo sting sem que estiver em "" ou ''

"""

nome = "Geek"
print(nome)
print(type(nome))

nome = "Geek \nTeste"
print(nome)
print(type(nome))

nome = "Geek University"
print(nome)
print(nome.upper())
print(nome.lower())
print(nome.split())

"""Internamente o python cria uma string em um array"""
# ["G","e","e","k"," ","U","n","i","v","e","r","s","i","t","y"]
nome = "Geek University"
print(nome[0])
print(nome[0:4])  # Slice de String
print(nome[5:15])

"""
Inverter String em python
[::-1] -> Comece do primeiro elemento, vá até o ultimo elemento, inverta
"""
print(nome[::-1])
print(nome[5:])

"""Replace"""
print(nome.replace("e", "i"))

"""Texto Palindromo (o inverso é ele mesmo)"""
texto = "socorram me subino onibus em marrocos"
print(texto)
print(texto[::-1])
