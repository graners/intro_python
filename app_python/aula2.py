a = 2
b = 5
soma = a + b
subtracao = a - b
multip = a * b
divis = a / b
resto = a % b
print(soma)
print(type(soma))
# soma = str(soma)  # casting integer to string
print('soma = ' + str(soma))  # concatena duas strings
print(type(soma))

print(subtracao)

print(multip)

print(divis)
print(type(divis))
print(int(divis))  # uma forma de arredondar um número decimal

print(resto)

# converter string para inteiro
x = '1'
soma2 = int(x) + a
print(soma2)

# forma mais utilizada de concatenar str com outro tipo
print('soma = {}. subtração = {}'.format(soma, subtracao))
print('soma = {so}. subtração = {su}. \nmultiplicação = {m}'.format(su=subtracao, m=multip, so=soma))

# para comentar mais de uma linha, usar ctrl + \

# Interagindo com o usuário
a = input('Digite um valor: ')
print(type(a))
# apesar de ter digitado um valor, o python entende que é um string
# é preciso fazer um casting da variável recebida
a = int(a)
b = int(input('Digite outro valor: '))  # primeiro, eu recebo um valor, depois eu faço o cast
soma = a + b
subtracao = a - b
multip = a * b
divis = a / b
resto = a % b
resultado = ('soma = {so}. subtração = {su}. \nmultiplicação = {m}.'
             ' \ndivisão = {d}. \nresto = {r}'.format(su=subtracao, m=multip, so=soma,
                                                      r=resto, d=divis))
print(resultado)
