# MÉTODOS E FUNÇÕES

# O conceito de função e método se diferenciam só e somente só pelo retorno de valores.
# Toda função é um bloco de instrução que, possui um nome único que a identifica em seu escopo, pode receber
# parâmetros e SEMPRE retorna um valor.
# Um método é um bloco de instrução, possui um nome único que o identifica em seu escopo, pode receber parâmetros
# e NUNCA retorna valores.
# http://excript.com/python/introducao-funcoes-python.html#:~:text=FUN%C3%87%C3%83O%20vs%20M%C3%89TODO&text=Toda%20fun%C3%A7%C3%A3o%20%C3%A9%20um%20bloco,par%C3%A2metros%20e%20NUNCA%20retorna%20valores.

# Função para realizar uma soma (pois retorna valor)
# def soma(a, b):
#     return a + b
#
#
# def subtracao(a, b):
#     return a - b
#
#
# def multiplicacao(a, b):
#     return a * b
#
#
# def divisao(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return 'Erro: divisão por zero.'
#
#
# # É necessário deixar duas linhas de espaço depois do término da função/método
# print(soma(5, 4))
# print(subtracao(4, 9))
# print(multiplicacao(2, 10.8))
# print(divisao(2, 2))


# CLASSES (por convenção, classe começa por letra maiúscula)
# Classes proporcionam uma forma de organizar dados e funcionalidades juntos. Criar uma nova classe cria um
# novo “tipo” de objeto, permitindo que novas “instâncias” desse tipo sejam produzidas. Cada instância da classe pode
# ter atributos anexados a ela, para manter o seu estado. Instâncias da classe também podem ter métodos (definidos pela
# classe) para modificar seu estado.
# https://docs.python.org/pt-br/3/tutorial/classes.html#:~:text=As%20classes%20em%20Python%20oferecem,m%C3%A9todo%20hom%C3%B4nimo%20de%20uma%20classe

class Calculadora:
    # A operação de instanciação (“invocar” um objeto classe) cria um objeto vazio. Muitas classes preferem criar
    # novos objetos com um estado inicial predeterminado. Quando uma classe define um método __init__(), o processo
    # de instanciação automaticamente invoca __init__() sobre a instância recém-criada. Sempre que a classe for
    # inicializada, passará pelo método init (construtor) self é para referenciar o próprio objeto nesse caso,
    # sempre que Calculadora for inicializada, será necessário passar dois parâmetros
    # SELF: o self é usado em classes no Python para indicar que você está referenciando alguma coisa do próprio
    # objeto (sejam eles atributos ou métodos) - na verdade, o self é o próprio objeto.
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    # Como os métodos estão dentro de uma classe, eles terão de usar o self para acessar os valores da classe
    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b

    def multiplicacao(self):
        return self.a * self.b

    def divisao(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return 'Erro: divisão por zero.'


if __name__ == '__main__':
    # Instanciando uma classe:
    calculadora = Calculadora(20, 0)
    print(calculadora.a)
    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.multiplicacao())
    print(calculadora.divisao())
