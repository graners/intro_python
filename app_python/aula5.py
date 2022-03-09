# LISTAS caracterizadas pelo uso de colchetes
lista = [1, 30, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante', 'peixe']
lista_variada = [1, 6, 3, 'papagaio']
# print(type(lista_variada))
# print(lista_animal[1])
#
# for x in lista_variada:
#     print(x)
#
#
# # Trabalhando com listas
# soma = 0
# for x in lista:
#     soma += x
# print(soma)
#
# print(sum(lista))  # outra forma...
#
# # Funciona com string ou numeros
# print(max(lista))  # maior valor da lista
# print(max(lista_animal))  # compara as letras em ordem alfabética
#
# print(min(lista))  # menor valor
# print(min(lista_animal))  # menor valor de letra em ordem alfabética
#
# # verificar se tem um elemento dentro de uma lista
# if 'gafanhoto' in lista_animal:
#     print('sim')
# else:
#     print('não')
#
# # Multiplicando listas
# nova_lista = lista_variada * 3
# print(nova_lista)
#
# # incluir um elemento a uma lista
# if 'gafanhoto' in lista_animal:
#     print('sim')
# else:
#     print('não')
#     lista_animal.append('gafanhoto')
# print(lista_animal)
#
# # tirar o último elemento da pilha
# lista_animal.pop()
# print(lista_animal)
#
# # tirar um elemento da lista passando a posição
# lista_animal.pop(1)
# print(lista_animal)
#
# # remover um elemento de uma lista a partir do nome
# lista_animal.remove('elefante')
# print(lista_animal)

# # Ordenando listas
# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
#
# lista_animal.reverse()
# print(lista_animal)

# Diferença lista x tupla
# Na lista, é possível alterar os elementos e sua ordem. Na tupla, não
lista_animal[0] = 'macaco'
print(lista_animal)

# TUPLA (não é possível alterar os objetos contidos nela)
tupla = (1, 15, 6, 78, 23)
print(type(tupla))
print(tupla)
print(tupla[1])  # consultar um elemento na posição x

# Quantidade de elementos
print(len(tupla))
print(len(lista))

# Converter uma lista em uma tupla
tupla_animal = tuple(lista_animal)
print(tupla_animal)

# Converter Tupla em Lista (útil se for necessário fazer uma alteração nos objetos)
# quando se opta por uma tupla, é porque não se quer alterar os objetos. se for para ficar alterando
# a melhor opção é trabalhar com lista
tupla_nome = ('Laís', "Roberto", 'Claudio', 'Renan')
print(type(tupla_nome))
print(tupla_nome)
lista_nome = list(tupla_nome)
print(type(lista_nome))
print(lista_nome)
