# UTILIZANDO CONDICIONAL IF ELIF ELSE
#
# a = int(input('Digite um número: '))
# b = int(input('Digite um número: '))
# c = int(input('Digite um número: '))
#
# # editar mais de uma linha por vez Alt + J ou usar o botão do meio do mouse
#
# # O Python trabalha com indentação ao invés de abrir e fechar chaves, como no C#, por exemplo
# # para a identação o tab tem valor de 4 espaços
# # if a > b:
# #     print("O maior número é {}".format(a))
# # print('Isto será escrito mesmo que o if seja falso porque está fora da indentação, portanto fora da condição.')
#
#
# if a > b and a > c:
#     print("O maior número é {}".format(a))
# elif b > c:  # elif é else com if
#     print("O maior número é {}".format(b))
# else:
#     print("O maior número é {}".format(c))


# # Descobrir se um número é par
# a = int(input('Digite um número: '))
# ehpar = a % 2
#
# if ehpar == 0:
#     print('{} é um número par.'.format(a))
# else:
#     print('{} é um número ímpar.'.format(a))

# Descobrir se há um par entre dois valores
a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
resto1 = a % 2
resto2 = b % 2

if resto1 == 0 and resto2 == 0:
    print('Os dois números são pares.')
elif resto1 == 0:
    print('{} é um número par e {} é ímpar'.format(a, b))
elif resto2 == 0:
    print('{} é um número par e {} é ímpar'.format(b, a))
else:
    print('Os dois números são ímpares.')

if resto1 == 0 or not resto2 > 0:
    print('Foi digitado um número par.')
else:
    print('Não foi digitado pelo menos um número par.')




