# # FOR
# # looping para imprimir 10 números. Começa no 0 e vai até 9
# for x in range(10):
#     print(x)
#
# # para determinar o número inicial:
# for x in range(1, 11):
#     print(x)

# # descobrir se um número é primo (minha solução):
# n = int(input('Digite um número: '))
# contador = 0
# for x in range(1, n + 1):
#     res = n % x
#     if res == 0:
#         contador += 1
#
# if contador == 2:
#     print('{} é um número primo.'.format(n))
# else:
#     print('{} não é um número primo.'.format(n))


# # números primos dentro de um intervalo:
# for x in range(1, 101):
#     contador = 0
#     for n in range(1, x + 1):
#         res = x % n
#         if res == 0:
#             contador += 1
#     if contador == 2:
#         print('{} é um número primo.'.format(x))


# # WHILE
# a = 0
# while a < 10:
#     print(a)
#     a += 1

total = 0
qt_notas = int(input('Quantas notas serão cadastradas? '))
for x in range(1, qt_notas + 1):
    nota = int(input(f'Digite a nota {x} do aluno: '))
    while nota > 10:
        nota = int(input('Nota inválida. Digite novamente: '))
    total += nota
print(f'A média da(s) {qt_notas} nota(s) é {total/qt_notas}.')
