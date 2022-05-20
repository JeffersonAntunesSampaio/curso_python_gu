"""
**kwargs

Poderiamos chamar este parametro de *xis, Mas por convenção,
utilizamos *kwargs para defini-lo

Este é só mais um parâmetro, mas diferente do *args que coloca os valores extras
em uma tupla, o **kwargs exige que utilizamos parâmetros nomeados, e trasnforma esses
parâmetros extras em um dicionário.
"""


# Exemplo
def cores_favoritas(**kwargs):
    for pessoal, cor in kwargs.items():
        print(f"A cor favorita de {pessoal.title()} é {cor.lower()}.")


cores_favoritas(jeff="Verde", juliana="Rosa", diogo="Azul", lipe="Roxo")


# OBS: Os parâmetros *args e **kwargs não são obrigatórios


# Exemplo mais complexo
def cumprimento_especial(**kwargs):
    if "geek" in kwargs and kwargs["geek"] == "Python":
        return "Você recebeu um cumprimento Pythônico Geek"
    elif "geek" in kwargs:
        return f"{kwargs['geek']} Geek!"
    return "Não tenho certeza quem você é..."


print(cumprimento_especial())
print(cumprimento_especial(geek="Python"))
print(cumprimento_especial(geek="oi"))
print(cumprimento_especial(geek="especial"))


# Nas nossas funções, podemos ter (NESTA ORDEM):
# - Parâmetros obrigatórios
# - *args
# - Parâmetros default (não obrigatórios)
# - *kwargs


def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f"{nome} tem {idade} anos")
    print(args)
    if solteiro:
        print("Solteiro")
    else:
        print("Casado")
    print(kwargs)


minha_funcao(27, "Jefferson")
minha_funcao(27, "Jefferson", 1, 2, 3, 4)
minha_funcao(27, "Jefferson", 1, 2, 3, 4, True)
minha_funcao(27, "Jefferson", 1, 2, 3, 4, solteiro=True, roles="Admin", logged=True)


# Desempacotar com **kwargs
def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {
    "nome": "Felicity",
    "sobrenome": "Jone"
}

print(mostra_nomes(**nomes))

