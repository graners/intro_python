# LÂMBDA E FUNÇÕES ANÔNIMAS

# só é eficiente para funções que resolvem problemas simples de uma linha, por exemplo. problemas mais complexos,
# fica bem mais difícil a implementação
# <nome_da_funcao> = lambda <lista_de_parametros>: <expressão>
# é preciso escrever lambda para definir uma função anônima

contador_letras = lambda lista_palavras: [len(palavra) for palavra in lista_palavras]
# como se lê: a função de nome 'contador_letras' é uma função lambda que recebe como parâmetro 'lista_palavras' e
# retorna uma lista com o tamanho de cada 'palavra' contida nessa lista
# [len(palavra) for palavra in lista_palavras] ===> para cada palavra contida em lista_palavras, verificar o tamanho
# e guardar esse valor em uma lista []
lista_animais = ['gato', 'cachorro']
print(contador_letras(lista_animais))

# soma = lambda a, b: a + b
# subtracao = lambda a, b: a - b
# print(soma(1, 2))


# DICIONÁRIO DE FUNÇÕES ANÔNIMAS
calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b
}
print(type(calculadora))
# para utilizar as funções anônimas dentro de um dicionário, é preciso atribuí-las a uma variável
# acessar o dicionário e suas funções:
soma = calculadora['soma']
subtracao = calculadora['subtracao']
multiplicacao = calculadora['multiplicacao']
divisao = calculadora['divisao']

print(soma(1, 5))
