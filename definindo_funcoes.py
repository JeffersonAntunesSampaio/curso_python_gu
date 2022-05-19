"""
Definindo Funções

DRY - Don't Repeat Yourself - Não repita você mesmo / Não repita seu código

Em Python a forma geral de definir função é:

def nome_da_funcao(parametros_de_entradas):
    bloco_da_funcao

- nome_da_função - SEMPRE com letras minusculas e se for composto, separado por underline (Snake Case)
- parametros_de_entradas - Opcionais, onde temos mais de um, cada um separado por virgula, podendo ser opicionais ou não
- bloco_da_funcao - Também chamado de corpo da função, ou implementação, nesse bloco pode ter retorno ou não.

OBS: Veja que para definir uma funçõa utilizamos a palavra reservada "def"

Definições
- Funções são pequenos partes de códigos que realizam tarefas especificas
- Pode ou não receber entradas de dados e retornar uma saída de dados
- Muito uteis para executar procedimenos similares por repetidas vezes

OSB: Se você escrever uma função que realiza várias taferas dentro dela, é
bom fazer uma verificação para que a função seja simplificada


Já utilizamos várias funções desde que iniciamos este curso:
- print()
- len()
- max()
- min()
- count()
- e muitas outras.
"""

# Exemplo de utilização de funções
cores = ["verde", "amarelo", "azul", "branco"]

# Utilizando a função integrada (Built-in) do Python print()
print(cores)

cores.append("roxo")
print(cores)

cores.clear()
print(cores)


# print(help(print))


# Definindo a primeira função
def diz_oi():
    print("oi!")


"""
OBS:
1 - Veja que, dentro das nossas funções podemos utilizar outras funções.
2 - Veja que nossa função só executa 1 tarefa, ou seja, a unica coisa que ela faz é dizer oi
3 - Veja que esta função não recebe nenhum dado de entrada
4 - Veja que esta função não retorna nada
"""

# Utilizando funções
diz_oi()  # Chamada de execução


# Exemplo 2
def cantar_parabens():
    print("Parabéns para você")
    print("Nesta data querida")
    print("Muitas felicidades")
    print("Muitos anos de vida")
    print("Viva o aniversariante!")


for n in range(2):
    cantar_parabens()


# Em Python, podemos inclusive criar variáveis do tipo de uma função e executar esta função.
canta = cantar_parabens

canta()
