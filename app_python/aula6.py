# # CONJUNTOS
# # https://algoritmosempython.com.br/cursos/programacao-python/conjuntos/
# # Para criar conjuntos, usa-se chaves: { }
# # Um set em Python é uma coleção de itens únicos (distintos).
#
# conjunto = {1, 7, 3, 5, 9}
# print(type(conjunto))  # resultado: set (que é 'conjunto' em inglês)
#
# # não existe duplicidade em um conjunto. Se colocar elemento iguais, eles serão ignorados e somente um deles será
# # considerado
# conjunto = {1, 2, 3, 4, 4, 4}
# print(conjunto)
#
# # Adicionar um novo elemento
# conjunto.add(5)
# print(conjunto)
#
# # Remover um elemento
# # remove só pode ser usada quando se tem certeza de que um elemento está no conjunto. Caso contrário, será disparada
# # uma exceção
# conjunto.remove(4)
# conjunto.discard(3)
# print(conjunto)

# # União de conjuntos
# conjunto = {1, 2, 3, 4}
# conjunto2 = {5, 6, 7, 8, 2}
# # conjunto_uniao = conjunto.union(conjunto2)
# # print(conjunto_uniao)
# # Outra forma de fazer união:
# conjunto_uniao = conjunto | conjunto2
# print(conjunto_uniao)
#
# # Interseção de conjuntos: retorna os elementos que aparecem em ambos conjuntos
# # conjunto_intersecao = conjunto & conjunto2
# conjunto_intersecao = conjunto.intersection(conjunto2)
# print(conjunto_intersecao)

# # Diferença de conjuntos: elementos diferentes
# A = {1, 2, 3, 5, 7}
# B = {2, 4, 6, 8, 1}
# diferenca = A - B
# print(diferenca)
# diferenca = B.difference(A)
# print(diferenca)
#
# # Diferença simétrica: A diferença simétrica entre os conjuntos A e B é o conjunto de todos os elementos que pertencem
# # à reunião dos conjuntos A e B e não pertencem à interseção dos conjuntos A e B.
# # A = {1, 2, 3, 5, 7}
# # B = {2, 4, 6, 8, 1}
# diferenca_simetrica = A.symmetric_difference(B)
# print(diferenca_simetrica)



# Pertinência: A relação de pertinência mostra se um elemento está dentro ou não de um conjunto, ou seja, se ele
# pertence ou não pertence a um conjunto.

# Função subset: retorne se um conjunto é subconjunto de outro conjunto
A = {1, 2, 3, 5}
B = {1, 2, 3, 5, 6}
subconjunto = A.issubset(B)
print(subconjunto)
subconjunto = B <= A  # outra forma de subset
print(subconjunto)

# Superset: The issuperset() method returns True if all items in the specified set exists in the original set, otherwise
# it returns False.
superconjunto = B.issuperset(A)
print(superconjunto)


# Convertendo uma lista para conjunto: serve para limpar uma lista com elementos em duplicidade
# Fácil e de baixo custo operacional
lista = ['macaco', 'gato', 'cachorro', 'macaco', 'gato']
conjunto = set(lista)
print(conjunto)

# Convertendo conjunto para lista
lista = list(conjunto)
print(lista)

# Convertendo tupla para conjunto
tupla = ('galo', 'gato', 'boi', 'boi')
conjunto = set(tupla)
print(conjunto)

# Convertendo de conjunto para tupla
tupla = tuple(conjunto)
print(tupla)
